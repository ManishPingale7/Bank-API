from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Bank, Branch


class BranchApiTests(APITestCase):

    def setUp(self):
        """Create sample data for tests."""
        bank = Bank.objects.create(name="State Bank of India", id=1)
        Branch.objects.create(ifsc="SBIN0001234", branch="Main Branch", address="123 Main St",
                              city="City", district="District", state="State", bank=bank)
        Branch.objects.create(ifsc="SBIN0005678", branch="Second Branch", address="456 Second St",
                              city="City", district="District", state="State", bank=bank)

    def test_get_all_banks(self):
        """Test GET all bank."""
        response = self.client.get('/api/bank/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # should have 1 bank in the response
        self.assertEqual(len(response.data), 1)

    def test_get_branch_by_ifsc(self):
        """Test GET a specific branch by IFSC."""
        response = self.client.get('/api/branch/SBIN0001234/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the IFSC matches
        self.assertEqual(response.data['ifsc'], 'SBIN0001234')
        # Check if branch name matches
        self.assertEqual(response.data['branch'], 'Main Branch')

    def test_get_branch_not_found(self):
        """Test GET a branch with an invalid IFSC."""
        response = self.client.get('/api/branches/INVALIDIFSC/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
