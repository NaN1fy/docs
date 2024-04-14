import sys
import re
import os

disclaimer = " \
# --------------------- \
# |    DISCLAIMER    | \
# --------------------- \
# Disclaimer: This script is not intended to achieve a 100% pass rate, as it will also consider terms within tables (like headers). However, it provides an excellent way to identify missing terms. \
# The decision not to implement checks for tables or links is due to potential edge cases where it's preferable to have more false positives than none at all. \
# --------------------- "

def find_tex_files(directory, filenames):
    paths = [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files if file.endswith('.tex') and not file.lower() == 'glossario.tex' and not os.path.abspath(os.path.join(root, file)).startswith(os.path.abspath(os.path.join(directory, 'template'))) and any(filename in os.path.join(root, file) for filename in filenames)]
    return paths

def find_glossary_path(base_directory):
    return next((os.path.join(root, file) for root, _, files in os.walk(base_directory) for file in files if file.lower() == "glossario.csv"), None)

def read_glossary(glossary_path):
    with open(glossary_path, 'r') as file:
        return {line.strip().split(';', 1)[0].lower() for line in file}

def find_glossary_errors(glossary_terms, document_paths):
    errors = {}
    for document_path in document_paths:
        with open(document_path, 'r') as file:
            document_text = file.read()
            terms_not_found = list(filter(lambda term: re.search(r'\b' + re.escape(term) + r'\b', document_text, re.IGNORECASE) and not re.search(r'\\glossterm\{' + re.escape(term) + r'\}', document_text, re.IGNORECASE) and not re.search(r'\\href\{[^{}]*?' + re.escape(term) + r'[^{}]*?\}', document_text), glossary_terms))
            if terms_not_found:
                errors[document_path] = terms_not_found
    return errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python check_glossary.py <file1.tex> <file2.tex> ...")

    print(disclaimer)
    base_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../documents"))

    glossary_path = find_glossary_path(base_directory)
    if not glossary_path:
        sys.exit("Glossary file not found.")

    document_paths = find_tex_files(base_directory, sys.argv[1:])

    glossary_terms = read_glossary(glossary_path)
    errors = find_glossary_errors(glossary_terms, document_paths)

    if errors:
        print("Glossary terms not formatted correctly in the following documents:")
        for document_path, terms in errors.items():
            print(f"- {document_path}: {', '.join(terms)}")
    else:
        print("No glossary terms found with incorrect formatting in the documents.")
