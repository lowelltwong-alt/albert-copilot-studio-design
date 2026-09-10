# Azure adapter: Container Apps → Copilot Studio / Foundry

This is a deployment recipe, not a tenant deployment receipt. Azure CLI, Docker and a tenant were unavailable in the build environment. Run the local tests first, then have an Azure owner review the image, network policy, secret store, data retention and identity before deploying.

## Build and deploy shape

Build a pinned image from the package root and publish it to an approved Azure Container Registry. Deploy `containerapp.bicep` into an existing Container Apps environment. The template uses an HTTPS ingress, exact host allowlist, API-key secrets and an Azure Files mount for the append-only candidate state. Use Key Vault or an approved secret reference in production; do not commit a parameter file containing real keys.

The API-key adapter is intentionally conservative. It authenticates `x-api-key` at the application boundary, separates the optional intake key, rejects unapproved hosts/origins and never exposes network review/promotion. If the organization requires Microsoft Entra/OAuth rather than a connection key, put a validated gateway in front of this adapter and re-run the auth and ingress acceptance tests; this package does not implement an Entra token verifier.

Example deployment outline:

```powershell
az acr build --registry <registry> --image digital-assets-mcp:1.0.0 --file Dockerfile .
az deployment group create --resource-group <resource-group> --template-file azure/containerapp.bicep --parameters @azure/parameters.example.json image=<registry>.azurecr.io/digital-assets-mcp:1.0.0
```

The command is illustrative. Fill in the existing environment, storage account/share and a secret delivery method approved by the tenant owner. Review the Bicep API version against the current Azure subscription before deployment.

## Copilot Studio

Create an MCP server connection for the deployed HTTPS URL ending in `/mcp`, choose **Streamable** transport, and select API-key authentication. Configure the header as `x-api-key` and store the reader key in the connection. Start with read-only tools. Enable candidate intake only after a separate connection/key and human review process is approved. Copilot Studio's current documentation says existing MCP servers use Streamable transport and supports API-key or OAuth configuration; tenant behavior, DLP and publication still need acceptance testing.

## Microsoft Foundry

Add an MCP tool to the agent or project with the same `/mcp` URL. Use the connection's API-key option with the `x-api-key` header, or place a reviewed gateway in front for Microsoft Entra/OAuth. Start with `SearchAssets`, `GetAsset`, `GetNeighbors`, `GetAssetContent`, `GetLifecycleStatus`, `GetRuntimeStatus` and `GetLessonCandidate`. The package does not grant the agent permission to write or promote lessons. Foundry's current documentation describes key-based, Entra and OAuth identity-passthrough options; this adapter implements only the key-based connection boundary.

## Cloud acceptance checklist

Record actual values and evidence in a private deployment receipt:

* TLS URL, exact host/origin allowlists and ingress policy;
* image digest and package `release`;
* reader/intake secret references (never their values);
* state mount write/read test and backup/retention plan;
* MCP initialize/list/call through Copilot Studio and Foundry;
* API parity and negative auth/host/body tests;
* DLP, logging redaction, rate limits and rollback owner;
* human decision for each candidate before any asset becomes reviewed guidance.

## Sources

* [Copilot Studio: connect an existing MCP server](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent)
* [Foundry: connect agents to MCP server endpoints](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol)
* [Azure Container Apps storage mounts](https://learn.microsoft.com/en-us/azure/container-apps/storage-mounts)

