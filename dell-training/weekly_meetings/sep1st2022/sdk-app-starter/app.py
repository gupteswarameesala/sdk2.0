import json
import sys

from generate_manifest import generateManifest
from python import *
from java import *
import os

try:
    destination_path = sys.argv[1]
    app_language = sys.argv[2]
    domain_json_path = sys.argv[3]
except (Exception,):
    destination_path = None
    app_language = None
    domain_json_path = None

try:
    generate_manifest = sys.argv[4]
except (Exception,):
    generate_manifest = None

current_path = os.getcwd()


def initialize_app_languge(destinationpath, applanguage, generatemanifest):
    if applanguage is not None and destinationpath is not None:
        if applanguage == "java":
            if generatemanifest is None or generatemanifest == "false":
                print(applanguage + " app will be generated")
                initialize_java_app(destinationpath, current_path, domain_json_path)
            else:
                if generatemanifest == "true":
                    print(applanguage + " manifest  will be generated")
                    domainJson = getDomainJson(domain_json_path)
                    generateManifest(domainJson, destinationpath, applanguage)

        elif applanguage == "python":
            if generatemanifest is None or generatemanifest == "false":
                print(applanguage + " app will be generated")
                initialize_python_app(destinationpath, current_path, domain_json_path)
            else:
                if generatemanifest == "true":
                    print(applanguage + " manifest  will be generated")
                    domainJson = getDomainJson(domain_json_path)
                    generateManifest(domainJson, destinationpath, applanguage)

    else:
        print("please provide app_language/generate_manifest and destination path fields")


def getDomainJson(filename):
    with open(filename) as domainFile:
        domainJson = json.load(domainFile)
    return domainJson


if __name__ == "__main__":
    initialize_app_languge(destination_path, app_language, generate_manifest)
