#! python3
# -*- coding: utf-8 -*-
import os
import subprocess


root_path = r'D:\TenTest'
template_path = r'D:\TenTest\template'


def create_model_file():
    for subdir, dirs, files in os.walk(root_path):
        for dirc in dirs:
            if dirc != '.idea':
                training_path = r'%s\%s\training.txt' % (root_path, dirc)
                model_path = r'%s\%s\model' % (root_path, dirc)
                print(training_path)
                print(model_path)
                subprocess.call("crf_learn %s %s %s" % (template_path, training_path, model_path))


def generate_output_file():
    for subdir, dirs, files in os.walk(root_path):
        for dirc in dirs:
            if dirc != '.idea' and dirc != 'inspectionProfiles':
                print(dirc)
                model_path = r'%s\%s\model' % (root_path, dirc)
                test_path = r'%s\%s\test.txt' % (root_path, dirc)
                output_path = r'%s\%s\output.txt' % (root_path, dirc)
                print(model_path)
                print(test_path)
                print(output_path)
                command = "crf_test -m %s %s > %s" % (model_path, test_path, output_path)
                os.system(command)  # 要生成输出文件时，用os.system


if __name__ == '__main__':
    create_model_file()
    generate_output_file()
