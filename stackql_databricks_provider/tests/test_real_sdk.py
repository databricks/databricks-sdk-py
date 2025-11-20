"""
Integration tests using real Databricks SDK dataclasses.
"""

import logging
import unittest

from stackql_databricks_provider.parser import (
    get_data_classes,
    get_schema_from_data_class,
)

# Set up logging
logging.basicConfig(level=logging.INFO)


class TestRealDatabricksSDK(unittest.TestCase):
    """Test with real Databricks SDK modules"""

    def test_get_data_classes_from_iam_service(self):
        """Test extracting dataclasses from the IAM service"""
        try:
            from databricks.sdk.service import iam

            dataclasses = get_data_classes(iam)

            # Should find multiple dataclasses
            self.assertGreater(len(dataclasses), 0)

            # Check for known dataclasses
            dataclass_names = [dc.__name__ for dc in dataclasses]
            print(f"\nFound {len(dataclasses)} dataclasses in iam service")
            print(f"Sample dataclasses: {dataclass_names[:10]}")

            # AccessControlRequest should be in there
            self.assertIn("AccessControlRequest", dataclass_names)

        except ImportError:
            self.skipTest("Databricks SDK not installed")

    def test_schema_from_access_control_request(self):
        """Test schema generation from AccessControlRequest"""
        try:
            from databricks.sdk.service.iam import AccessControlRequest

            schema = get_schema_from_data_class(None, AccessControlRequest)

            print("\n" + "=" * 80)
            print("AccessControlRequest Schema:")
            print("=" * 80)
            import json

            print(json.dumps(schema, indent=2))

            # Verify structure
            self.assertIn("AccessControlRequest", schema)
            self.assertEqual(schema["AccessControlRequest"]["type"], "object")

            # Should have properties
            properties = schema["AccessControlRequest"]["properties"]
            self.assertGreater(len(properties), 0)

            # Check for known fields
            self.assertIn("group_name", properties)
            self.assertIn("permission_level", properties)

            # permission_level should be an enum
            if "enum" in properties["permission_level"]:
                print(
                    f"\nPermission level enum values: {properties['permission_level']['enum']}"
                )

            # All fields should be optional (have defaults)
            required = schema["AccessControlRequest"].get("required", [])
            print(f"\nRequired fields: {required}")

        except ImportError:
            self.skipTest("Databricks SDK not installed")

    def test_schema_from_cluster_policy(self):
        """Test schema generation from a compute service dataclass"""
        try:
            from databricks.sdk.service.compute import CreatePolicy

            schema = get_schema_from_data_class(None, CreatePolicy)

            print("\n" + "=" * 80)
            print("CreatePolicy Schema:")
            print("=" * 80)
            import json

            print(json.dumps(schema, indent=2))

            # Verify structure
            self.assertIn("CreatePolicy", schema)
            properties = schema["CreatePolicy"]["properties"]

            # Check for known fields
            if "name" in properties:
                print(f"\nName field: {properties['name']}")

        except ImportError:
            self.skipTest("Databricks SDK not installed")

    def test_schema_from_cluster_spec(self):
        """Test schema generation from ClusterSpec (complex nested structure)"""
        try:
            from databricks.sdk.service.compute import ClusterSpec

            schema = get_schema_from_data_class(None, ClusterSpec)

            print("\n" + "=" * 80)
            print("ClusterSpec Schema:")
            print("=" * 80)
            import json

            print(json.dumps(schema, indent=2))

            # Verify structure
            self.assertIn("ClusterSpec", schema)
            properties = schema["ClusterSpec"]["properties"]

            # Should have many properties
            self.assertGreater(len(properties), 5)

            # Check for some known complex fields
            print(f"\nTotal properties: {len(properties)}")
            print(f"Sample property names: {list(properties.keys())[:10]}")

        except ImportError:
            self.skipTest("Databricks SDK not installed")

    def test_get_data_classes_from_jobs_service(self):
        """Test extracting dataclasses from the jobs service"""
        try:
            from databricks.sdk.service import jobs

            dataclasses = get_data_classes(jobs)

            # Should find many dataclasses
            self.assertGreater(len(dataclasses), 10)

            dataclass_names = [dc.__name__ for dc in dataclasses]
            print(f"\nFound {len(dataclasses)} dataclasses in jobs service")

            # Check for known dataclasses
            self.assertIn("Job", dataclass_names)

            # Test schema generation for a few
            from databricks.sdk.service.jobs import Job

            schema = get_schema_from_data_class(jobs, Job)

            print("\n" + "=" * 80)
            print("Job Schema (first 5 properties):")
            print("=" * 80)
            import json

            properties = schema["Job"]["properties"]
            sample_props = dict(list(properties.items())[:5])
            print(json.dumps({"Job": {"properties": sample_props}}, indent=2))
            print(f"... and {len(properties) - 5} more properties")

        except ImportError:
            self.skipTest("Databricks SDK not installed")


if __name__ == "__main__":
    unittest.main(verbosity=2)
