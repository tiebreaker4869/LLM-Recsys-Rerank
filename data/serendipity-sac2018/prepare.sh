#!/bin/bash

wget https://files.grouplens.org/datasets/serendipity-sac2018/serendipity-sac2018.zip

unzip serendipity-sac2018.zip

mv serendipity-sac2018/* ./

rm -rf serendipity-sac2018 serendipity-sac2018.zip