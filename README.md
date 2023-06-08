<h1 align="center"><img src="https://github.com/Teebra/aws/raw/master/images/aws.png" alt="AWS" width=130 height=130></h1>

<h2 align="center">cloud-native-monitoring-app with <a href="https://aws.amazon.com/" target="_blank">Amazon Web Services</a> using the <a href="https://aws.amazon.com/cli/" target="_blank">AWS CLI</a> and <a href="https://eksctl.io/" target="_blank">eksctl</a>.</h2>

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://shields.io/)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)

This repository contains Cloud Native Monitoring App which monitor CPU and Memory usages

## Table of contents

- [Why](#why)
- [Getting Started](#getting-started)
- [What's Included](#tools-included-in-this-repo)
- [Bugs and Feature Requests](#bugs-and-feature-requests)
- [Creator](#creator)
- [Copyright and License](#copyright-and-license)

## Why

## Getting Started

### What is the AWS Command Line Interface?

The AWS CLI is an open source tool built on top of the AWS SDK for Python (Boto) that provides commands for interacting with AWS services.
[Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html)

**Requirements:**
* Python 3 version 3.3+
* macOS, Linux, or Unix

If you already have pip and a supported version of Python, you can install the AWS CLI with the following command:

`$ pip install awscli --upgrade --user`

[Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

For general use, the aws configure command is the fastest way to set up your AWS CLI installation.

`$ aws configure`

The AWS CLI will prompt you for four pieces of information. AWS Access Key ID and AWS Secret Access Key are your account credentials.

[Named Profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-multiple-profiles.html)

The AWS CLI supports named profiles stored in the config and credentials files. You can configure additional profiles by using `aws configure` with the `--profile option` or by adding entries to the config and credentials files.

`$ aws configure --profile example`
