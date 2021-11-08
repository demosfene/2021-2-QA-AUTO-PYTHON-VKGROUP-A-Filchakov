import items as items
import pytest

from test_api.base import ApiBase


class TestApi(ApiBase):
    authorize = False

    @pytest.mark.UI
    def test_valid_login_my(self):
        assert self.api_client.login()

    @pytest.mark.UI
    def test_create_campaign(self):
        self.api_client.login()
        campaign_id = self.api_client.create_campaign()
        campaign = self.api_client.get_campaign(campaign_id)
        assert campaign['status'] == 'active'
        self.api_client.delete_campaign(campaign_id)

    @pytest.mark.UI
    def test_create_segment(self):
        self.api_client.login()
        segment_id = self.api_client.create_segment()
        segment = self.api_client.get_segment(segment_id).json()['id']
        assert segment == segment_id
        self.api_client.delete_segment(segment_id)

    @pytest.mark.UI
    def test_delete_segment(self):
        self.api_client.login()
        segment_id = self.api_client.create_segment()
        self.api_client.delete_segment(segment_id)
        segment = self.api_client.get_segment(segment_id)
        assert segment.status_code == 404

    @pytest.mark.UI
    def test_delete_campaign(self):
        self.api_client.login()
        campaign_id = self.api_client.create_campaign()
        self.api_client.delete_campaign(campaign_id)
        campaign = self.api_client.get_campaign(campaign_id)
        assert campaign['status'] == 'deleted'
