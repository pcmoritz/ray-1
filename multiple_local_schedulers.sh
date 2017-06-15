#!/bin/bash
# for i in {1..100}
# do
#   python test/runtest.py ResourcesTest.testMultipleLocalSchedulers
# done

for i in {1..100}
do
  python test/component_failures_test.py ComponentFailureTest.testPlasmaStoreFailed
done
