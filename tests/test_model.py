""" Unittests for API model """
import json
from datetime import datetime, timedelta
import pytest
from to_do_app.task import TaskCollection
from to_do_app.model import setup_app, close_app
__author__ = "Marcus Bakke"

@pytest.fixture(name="expected")
def fixture_expected():
    """Fixture to build payload for POST"""
    # Add some data
    payloads = []
    status = ['COMPLETED', 'ACTIVE']
    for ind in range(1, 6):
        start_date = datetime.strptime('2022-06-15', '%Y-%m-%d')
        if ind != 5:
            due_date = start_date + timedelta(days=ind)
        else:
            due_date = start_date - timedelta(days=ind)
        payloads.append(json.dumps(dict(
            task_id=ind,
            name='Task '+str(ind),
            description='Description '+str(ind),
            priority=str(ind),
            start_date=start_date.strftime('%Y-%m-%d'),
            due_date=due_date.strftime('%Y-%m-%d'),
            status=status[ind % 2],
            closed_date=datetime.today().strftime('%Y-%m-%d'),
        )))
    return payloads

@pytest.fixture(name="client")
def fixture_client(mocker, expected):
    """Initialize test app"""
    # Setup mocker to in-memory database
    mocker.patch('to_do_app.model.task_collection', TaskCollection(path='sqlite://'))
    # Build test app
    app, database = setup_app(path='sqlite://')
    app = app.test_client()
    # Add some data
    for payload in expected:
        app.post(
            '/tasks',
            headers={"Content-Type": "application/json"},
            data=payload,
        )
    yield app
    close_app(database)


class TestModelGet:
    """Unittest class for model GET resources"""

    @staticmethod
    def api_get(client, url: str):
        """Method to call get function with appropriate URL"""
        return client.get(url)

    def test_task(self, client, expected):
        """test task view"""
        response = self.api_get(client, '/tasks')
        assert response.status_code == 200
        assert len(expected) == len(response.json['data'])
        out = response.json['data']
        order = range(0, 5)
        for ind in order:
            expect = json.loads(expected[ind])
            expect['priority'] = int(expect['priority'])
            assert expect == out[ind]

    def test_priority(self, client, expected):
        """test priority view"""
        response = self.api_get(client, '/priority')
        assert response.status_code == 200
        assert len(expected) == len(response.json['data'])
        order = range(0, 5)
        out = response.json['data']
        for ind in order[::-1]:
            expect = json.loads(expected[ind])
            expect['priority'] = int(expect['priority'])
            assert expect == out[len(order)-ind-1]

    def test_duedate(self, client, expected):
        """test duedate view"""
        response = self.api_get(client, '/due_date')
        assert response.status_code == 200
        assert len(expected) == len(response.json['data'])
        out = response.json['data']
        expect_order = range(0, 5)
        order = [1, 2, 3, 4, 0]
        for ind in expect_order:
            expect = json.loads(expected[ind])
            expect['priority'] = int(expect['priority'])
            assert expect == out[order[ind]]

    def test_overdue(self, client, expected):
        """test overdue view"""
        response = self.api_get(client, '/overdue')
        assert response.status_code == 200
        expect = json.loads(expected[4])
        expect['priority'] = int(expect['priority'])
        out = response.json['data'][0]
        assert expect == out

class TestModelPost:
    """Unittest class for model POST resources"""

    @staticmethod
    def api_post(client, url: str, payload):
        """Method to call post function with appropriate URL and payload"""
        return client.post(
            url,
            headers={"Content-Type": "application/json"},
            data=payload
        )

    def test_task(self, client):
        """test task view"""
        ind = 6
        payload = json.dumps(dict(
            task_id=ind,
            name='Task '+str(ind),
            description='Description '+str(ind),
            priority=str(ind),
            status='ACTIVE',
        ))
        response = self.api_post(client, '/tasks', payload)
        assert response.status_code == 200
        response = TestModelGet.api_get(client, '/tasks')
        assert 6 == len(response.json['data'])
        expect = json.loads(payload)
        expect['priority'] = int(expect['priority'])
        expect['start_date'] = datetime.today().strftime('%Y-%m-%d')
        expect['due_date'] = (datetime.today()+timedelta(weeks=1)).strftime('%Y-%m-%d')
        expect['closed_date'] = None
        out = response.json['data'][-1]
        assert expect == out
        