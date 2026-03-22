# Test Environment Instructions

This directory contains resources to spin up an isolated environment suitable for testing WAF bypass techniques locally without risking production environments.

## Prerequisites

- Docker
- Docker Compose

## Quick Start (ModSecurity CRS)

To spin up a default NGINX reverse-proxy armed with ModSecurity and the OWASP Core Rule Set, protecting a vulnerable DVWA instance:

\`\`\`bash
# Build and run the environment
docker-compose up -d
\`\`\`

The vulnerable application will be available at `http://localhost:8080/`. The WAF intercepts traffic on port `8080`.

## Architecture

*   **Reverse Proxy / WAF (`nginx-modsec`)**:
    An NGINX container configured with `libmodsecurity3`. Rules are mapped from `docker/modsec-rules/`.
*   **Web Application Server (`backend-dvwa`)**:
    Damn Vulnerable Web Application. Serves as our target for XSS, SQLi, and Command Injection payloads.

## Rule Testing

To test how specific rules behave:
1. Examine the `docker/modsec-rules/crs-setup.conf` configuration file.
2. The default set runs in Paranoia Level 1.
3. Tail the WAF logs to observe real-time blocks:
   \`docker logs -f nginx-modsec | grep "ModSecurity: Access denied"\`

## Tearing Down

\`\`\`bash
docker-compose down -v
\`\`\`
