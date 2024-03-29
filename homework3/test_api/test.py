import json

import pytest

from test_api.base import ApiBase


class TestApi(ApiBase):
    authorize = False

    @pytest.mark.API
    def test_valid_login_my(self):
        assert self.api_client.login()

    @pytest.mark.API
    def test_create_campaign(self):
        self.api_client.login()
        campaign_info = self.api_client.create_campaign()
        campaign_response = campaign_info['response']
        campaign_name = campaign_info['campaign_name']
        assert campaign_response.status_code == 200
        campaign_id = json.loads(campaign_response.text)
        campaign = self.api_client.get_campaign(campaign_id)
        assert campaign.status_code == 200
        assert campaign.json()['status'] == 'active'
        assert campaign.json()['name'] == campaign_name
        self.api_client.delete_campaign(campaign_id)

    @pytest.mark.API
    def test_create_segment(self):
        self.api_client.login()
        segment_info = self.api_client.create_segment()
        segment_response = segment_info['response']
        segment_name = segment_info['segment_name']
        assert segment_response.status_code == 200
        segment_id = json.loads(segment_response.text)["id"]
        segment = self.api_client.get_segment(segment_id)
        assert segment.status_code == 200
        segment_received_id = segment.json()['id']
        assert segment_received_id == segment_id
        segment_received_name = segment.json()['name']
        assert segment_received_name == segment_name
        self.api_client.delete_segment(segment_id)

    @pytest.mark.API
    def test_delete_segment(self):
        self.api_client.login()
        segment_info = self.api_client.create_segment()
        segment_response = segment_info['response']
        assert segment_response.status_code == 200
        segment_id = json.loads(segment_response.text)["id"]
        segment = self.api_client.delete_segment(segment_id)
        assert segment.status_code == 204
        segment_get = self.api_client.get_segment(segment_id)
        assert segment_get.status_code == 404

    @pytest.mark.API
    def test_delete_campaign(self):
        self.api_client.login()
        campaign_info = self.api_client.create_campaign()
        campaign_response = campaign_info['response']
        assert campaign_response.status_code == 200
        campaign_id = json.loads(campaign_response.text)
        campaign_delete_response = self.api_client.delete_campaign(campaign_id)
        assert campaign_delete_response.status_code == 204
        campaign_received = self.api_client.get_campaign(campaign_id)
        assert campaign_received.status_code == 200
        assert campaign_received.json()['status'] == 'deleted'
