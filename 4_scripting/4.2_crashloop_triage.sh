#!/bin/bash
set -eo pipefail

echo "CrashLoopBackOff Diagnostics"
echo "============================"

kubectl get pods -A --field-selector='status.phase==Running' \
  -o jsonpath='{range .items[?(@.status.containerStatuses[0].state.waiting.reason=="CrashLoopBackOff")]}'
    {"namespace": "{.metadata.namespace}", "pod": "{.metadata.name}", 
     "image": "{.spec.containers[0].image}", "restarts": "{.status.containerStatuses[0].restartCount}"}
{end}' | jq -s '.[]' | while read -r pod; do

    ns=$(echo "$pod" | jq -r '.namespace')
    name=$(echo "$pod" | jq -r '.pod')
    image=$(echo "$pod" | jq -r '.image')
    restarts=$(echo "$pod" | jq -r '.restarts')

    echo -e "\nPod: $name (Namespace: $ns)"
    echo "Image: $image | Restarts: $restarts"
    echo "--------------------------------"
    
    echo "Current Logs:"
    kubectl logs -n "$ns" "$name" --tail=10 || echo "No logs"
    
    echo -e "\nPrevious Crash Logs:"
    kubectl logs -n "$ns" "$name" --previous --tail=10 2>/dev/null || 
      echo "No previous logs"
done