# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from django.test import TestCase,Client

from django.contrib.auth.models import User

from domains.models import Domain

from mailboxes.models import Mailbox, Alias

# Create your tests here.

class MailboxTest(unittest.TestCase):
    def setUp(self):
        self.domain = Domain.objects.create(name='test123123123.com',owner_id='1')
        Mailbox.objects.create(name='test1',password='test123',domain=self.domain)
        Alias.objects.create(name='testalias', domain=self.domain, to_mailbox='test@notuser.com')
        self.client = Client()

    def test_mailbox_create(self):
        Mailbox.objects.create(name='test_create',password='test456',domain=self.domain)
        mb_lookup = Mailbox.objects.filter(name='test_create', domain=self.domain).count()
        self.assertEqual(mb_lookup, 1)

    def test_mailbox_exists(self):
        mb_lookup = Mailbox.objects.filter(name='test1', domain=self.domain).count()
        self.assertEqual(mb_lookup, 1)

    def test_alias_exists(self):
        alias_lookup = Alias.objects.filter(domain=self.domain).filter(name='testalias').count()
        self.assertEqual(alias_lookup, 1)

    def test_list_mailboxes(self):
        response = self.client.get('/mailboxes/list/test123123123.com')

        self.assertEqual(response.status_code, 200)

    def test_create_mailbox(self):
        response = self.client.get('/mailboxes/create')
        self.assertEqual(resposne.status_code, 200)

    def test_mailbox_delete(self):
        Mailbox.objects.filter(name='test1').filter(domain=self.domain).delete()
        mb_lookup = Mailbox.objects.filter(name='test1').filter(domain=self.domain).count()

        self.assertEqual(mb_lookup, 0)

    def test_alias_delete(self):
        Alias.objects.get(name='testalias').delete()
        alias_lookup = Alias.objects.all().count()
        self.assertEqual(alias_lookup, 0)

    def test_domain_delete(self):
        class DomainTest(TestCase):
    def setUp(selt):
            User.objects.create_user('test', 'test@user.com', 'test123')
            Domain.objects.create(name='test.com',owner_id='1')
            ForwardDomain.objects.create(name='forwardtest.com', owner_id='1', to_domain_id='1')

    def test_domain_exists(self):
        domain_lookup = Domain.objects.filter(name='test.com').count()
        self.assertEqual(domain_lookup,1)

    def test_forward_domain_exists(self):
        fwd_domain_lookup = ForwardDomain.objects.filter(name='forwardtest.com').count()
        self.assertEqual(fwd_domain_lookup, 1)

    def test_domain_delete(self):
        Domain.objects.filter(domain=self.domain).delete()



