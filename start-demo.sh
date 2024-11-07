#!/bin/bash
set -e

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ANKAIOS_LOG_DIR="/workspaces/shift2sdv/.logs"

mkdir -p "$ANKAIOS_LOG_DIR"

echo "Staring up Ankaios server with TLS disabled"
RUST_LOG=debug ank-server --insecure --startup-config /workspaces/shift2sdv/shift2sdv_manifest.yaml 2> "$ANKAIOS_LOG_DIR/ank-server" &

echo "Staring up Ankaios agent hpc1 with TLS disabled"
RUST_LOG=debug ank-agent --insecure --name hpc1 2> "$ANKAIOS_LOG_DIR/ank-agent-hpc1" &

echo "Staring up Ankaios agent hpc2 with TLS disabled"
RUST_LOG=debug ank-agent --insecure --name hpc2 2> "$ANKAIOS_LOG_DIR/ank-agent-hpc2" &
