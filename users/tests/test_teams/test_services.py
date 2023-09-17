from django.test import TestCase

from users.exceptions import (
    TeamMemberAlreadyExistsError,
    TeamDoesNotExistError,
    TeamMemberDoesNotExistError,
)
from users.models import User, Team, TeamMember
from users.services.teams import (
    create_team,
    create_team_member,
    delete_team_by_id,
    delete_team_member_by_id,
)
from users.tests.test_teams.factories import TeamFactory, TeamMemberFactory


class TeamCreateServicesTests(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            id=123456789,
            fullname='Eldos',
            username='usbtypec',
        )

    def test_create_team(self):
        team = create_team(
            user_id=self.user.id,
            name='Bulls',
        )
        self.assertEqual(team.name, 'Bulls')
        self.assertEqual(team.teammember_set.count(), 1)
        self.assertEqual(team.teammember_set.first().user, self.user)


class TeamDeleteServicesTests(TestCase):

    def setUp(self) -> None:
        self.team = TeamFactory()

    def test_delete_team_by_id(self) -> None:
        delete_team_by_id(self.team.id)
        self.assertEqual(Team.objects.count(), 0)

    def test_delete_team_by_id_does_not_exist_error(self) -> None:
        with self.assertRaises(TeamDoesNotExistError):
            delete_team_by_id(123456789)


class TeamMemberCreateServicesTests(TestCase):

    def setUp(self) -> None:
        self.eldos = User.objects.create(
            id=123456789,
            fullname='Eldos',
            username='usbtypec',
        )
        self.alex = User.objects.create(
            id=987654321,
            fullname='Alex',
            username='alex',
        )
        self.team = create_team(
            user_id=self.eldos.id,
            name='Bulls',
        )

    def test_create_team_member(self):
        team_member = create_team_member(
            team_id=self.team.id,
            user_id=self.alex.id,
        )
        self.assertEqual(team_member.team, self.team)
        self.assertEqual(team_member.user, self.alex)
        self.assertEqual(team_member.status, team_member.Status.MEMBER)

    def test_create_team_owner_as_member(self):
        # owner is already a member
        with self.assertRaises(TeamMemberAlreadyExistsError):
            create_team_member(
                team_id=self.team.id,
                user_id=self.eldos.id,
            )


class TeamMemberDeleteServicesTests(TestCase):

    def setUp(self) -> None:
        self.team_member = TeamMemberFactory()

    def test_delete_team_member_by_id(self) -> None:
        delete_team_member_by_id(self.team_member.id)
        self.assertEqual(TeamMember.objects.count(), 0)

        with self.assertRaises(TeamMemberDoesNotExistError):
            delete_team_member_by_id(self.team_member.id)

    def test_delete_team_member_by_id_does_not_exist_error(self) -> None:
        with self.assertRaises(TeamMemberDoesNotExistError):
            delete_team_member_by_id(123456789)
