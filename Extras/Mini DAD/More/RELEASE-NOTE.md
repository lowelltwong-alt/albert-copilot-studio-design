# Public presentation edition — 2026-09-10

The runtime, catalog and asset content are unchanged from the standalone 1.0 package. This edition adds a consolidated setup README and a proprietary license notice, and makes the Python test command machine-independent. ORIGINAL-PACKAGE-CONTENTS.json records the earlier archive; it is historical evidence, not the manifest for this edition.

Fresh verification: six core/stdio tests and four real HTTP tests passed. The HTTP test run used the existing pinned task-local dependencies with Windows extension paths. A normal dependency installation is expected to configure those paths; validate your own environment. No Azure or Copilot Studio tenant acceptance is claimed.
