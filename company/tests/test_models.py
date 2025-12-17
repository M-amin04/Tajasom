from django.test import TestCase
from company.models import CompanyHistory, TeamMember, CompanyInfo, Client, CompanyContact


class CompanyHistoryModelTest(TestCase):
    def test_create_history(self):
        history = CompanyHistory.objects.create(
            year='1400',
            title='تاسیس شرکت',
            description='شرکت تاسیس شد'
        )
        self.assertEqual(history.year, '1400')
        self.assertEqual(history.title, 'تاسیس شرکت')
        self.assertTrue(history.is_active)


class TeamMemberModelTest(TestCase):
    def test_create_team_member(self):
        member = TeamMember.objects.create(
            name='علی احمدی',
            position='مدیر فنی',
            image='team/test.jpg'
        )
        self.assertEqual(member.name, 'علی احمدی')
        self.assertEqual(member.position, 'مدیر فنی')


class CompanyInfoModelTest(TestCase):
    def test_create_company_info(self):
        info = CompanyInfo.objects.create(
            name='شرکت تجسم',
            description='شرکت مهندسی',
            years_experience=10,
            completed_projects=50
        )
        self.assertEqual(info.name, 'شرکت تجسم')
        self.assertEqual(info.years_experience, 10)
        self.assertEqual(info.completed_projects, 50)


class ClientModelTest(TestCase):
    def test_create_client(self):
        client = Client.objects.create(
            name='شرکت نفت',
            logo='clients/oil.jpg'
        )
        self.assertEqual(client.name, 'شرکت نفت')
        self.assertTrue(client.is_active)


class CompanyContactModelTest(TestCase):
    def test_create_company_contact(self):
        contact = CompanyContact.objects.create(
            address='تهران، میدان آزادی',
            phone='021-12345678',
            email='info@tajasom.com',
            working_hours='شنبه تا چهارشنبه ۸-۱۷'
        )
        self.assertEqual(contact.email, 'info@tajasom.com')
        self.assertEqual(contact.phone, '021-12345678')