### **4. Python & Bash Scripting**
#### **4.1 Kubernetes Config Validator (`k8s_validator.py`)**
```python
#!/usr/bin/env python3
import os
import yaml
import json
import argparse
from typing import List, Dict

def validate_doc(doc: Dict, file_path: str, doc_index: int) -> List[Dict]:
    errors = []
    for field in ['apiVersion', 'kind', 'metadata']:
        if field not in doc:
            errors.append({
                'file': file_path,
                'doc_index': doc_index,
                'error': f'Missing required field: {field}'
            })
        elif field == 'metadata' and 'name' not in doc['metadata']:
            errors.append({
                'file': file_path,
                'doc_index': doc_index,
                'error': 'Missing metadata.name'
            })
    return errors

def main():
    parser = argparse.ArgumentParser(description='Validate Kubernetes YAMLs')
    parser.add_argument('directory', help='Directory to scan')
    args = parser.parse_args()

    all_errors = []
    for root, _, files in os.walk(args.directory):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                path = os.path.join(root, file)
                try:
                    with open(path) as f:
                        for i, doc in enumerate(yaml.safe_load_all(f)):
                            if doc:
                                all_errors.extend(validate_doc(doc, path, i))
                except Exception as e:
                    all_errors.append({
                        'file': path,
                        'error': f'YAML error: {str(e)}'
                    })

    print(json.dumps(all_errors, indent=2))
    sys.exit(1 if all_errors else 0)

if __name__ == '__main__':
    import sys
    main()