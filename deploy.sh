#!/bin/bash

stage=$1

if [ "$stage" == "" ]
then
    exit -1
fi

source env.config

rm -rf package
mkdir package
pip install -r requirements.txt -t package
npm run build
cp -r ./server package/
cp -r ./dist package/
cp serverless.yml package/

find . -name "*.pyc" -exec rm -f {} \;


cd package && sls deploy --stage $stage \
	--security-group $security_group \
	--subnet-a $subnet_a --subnet-b $subnet_b --subnet-c $subnet_c

cd .. && rm -rf package && rm -rf dist