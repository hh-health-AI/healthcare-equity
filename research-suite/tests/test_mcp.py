"""Real stdio protocol checks. Skipped when the optional SDK is not installed."""
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(importlib.util.find_spec("mcp"), "optional MCP SDK not installed")
class McpTests(unittest.IsolatedAsyncioTestCase):
    async def test_stdio_initialize_list_calculate_and_reject_invalid(self):
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client
        server = StdioServerParameters(command=sys.executable, args=["-m", "hh_research.mcp_server"], cwd=str(ROOT))
        async with stdio_client(server) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                listed = await session.list_tools()
                self.assertEqual(len(listed.tools), 13)
                names = {t.name for t in listed.tools}
                self.assertIn("get_clinical_trial", names)
                packet = json.loads((ROOT / "examples/valuation.json").read_text())
                result = await session.call_tool("calculate_rnpv", {"packet": packet})
                self.assertFalse(result.isError)
                text = "".join(c.text for c in result.content if c.type == "text")
                self.assertIn("72.013", text)
                invalid = await session.call_tool("calculate_rnpv", {"packet": {}})
                self.assertTrue(invalid.isError)


if __name__ == "__main__":
    unittest.main()
