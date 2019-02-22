#!/bin/bash

set -e

echo Export dist

mkdir -p dist

p4a export_dist \
--release \
--sdk_dir=/home/tribler/Android/Sdk \
--ndk_dir=/home/tribler/Android/android-ndk-r13b \
--ndk_version=13 \
--android_api=18 \
--arch=armeabi-v7a \
--dist_name=IPV8Service \
--bootstrap=service_only \
--requirements=loader \
./dist
