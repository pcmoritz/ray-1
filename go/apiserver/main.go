package main

import (
     "context"
     "flag"
     "fmt"
     "net"
     "net/http"
     "os"

     "github.com/golang/glog"
     "google.golang.org/grpc"
     "google.golang.org/grpc/credentials/insecure"
     "github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
     "github.com/ray-project/ray/go/apiserver/proto"
)

var (
     port = flag.Int("port", 50051, "The server port")
)

type server struct {
     proto.UnimplementedApiServiceServer
}

func newServer() (*server, error) {
     return &server{}, nil
}

func (s *server) ListActors(ctx context.Context, msg *proto.ListActorsRequest) (*proto.ListActorsReply, error) {
    return &proto.ListActorsReply{}, nil
}

func runGrpcService(ctx context.Context, network, address string) error {
     l, err := net.Listen(network, address)
     if err != nil {
          return err
     }
     defer func() {
     if err := l.Close(); err != nil {
         glog.Errorf("failed to close %s %s: %v", network, address, err)
     }
     }()

     s := grpc.NewServer()
     server, err := newServer()
     if err != nil {
          return fmt.Errorf("failed creating server: %v", err)
     }
     proto.RegisterApiServiceServer(s, server)
     if err := s.Serve(l); err != nil {
          glog.Fatalf("failed to serve: %v", err)
     }
     return nil
}

func runInProcessGateway(ctx context.Context, address string) error {
     mux := runtime.NewServeMux()
     opts := []grpc.DialOption{grpc.WithTransportCredentials(insecure.NewCredentials())}
     err := proto.RegisterApiServiceHandlerFromEndpoint(ctx, mux, fmt.Sprintf("localhost:%d", *port), opts)
     if err != nil {
         return err
     }
     return http.ListenAndServe(address, mux)
}

func runServers(ctx context.Context) <-chan error {
     ch := make(chan error, 2)
     go func() {
          if err := runGrpcService(ctx, "tcp", fmt.Sprintf(":%d", *port)); err != nil {
               ch <- fmt.Errorf("cannot run grpc service: %v", err)
          }
     }()
     go func() {
          if err := runInProcessGateway(ctx, ":8081"); err != nil {
               ch <- fmt.Errorf("cannot run in process gateway service: %v", err)
          }
     }()
     return ch
}

func main() {
     flag.Parse()

     ctx, cancel := context.WithCancel(context.Background())
     defer cancel()

     errCh := runServers(ctx)
     select {
     case err := <-errCh:
          fmt.Fprintln(os.Stderr, err)
          os.Exit(1)
     }
}