import datetime

from dateutil.tz import tzutc

boost = {'_pagination_prev': {'_pagination_endpoint': '/api/v1/accounts/6717/statuses',
                              '_pagination_method': 'GET',
                              'since_id': 98972270904179914},
         'account': {'acct': 'moatest',
                     'avatar': 'https://pdx.social/avatars/original/missing.png',
                     'avatar_static': 'https://pdx.social/avatars/original/missing.png',
                     'created_at': datetime.datetime(2017, 10, 30, 20, 34, 29, 216000, tzinfo=tzutc()),
                     'display_name': '',
                     'followers_count': 0,
                     'following_count': 2,
                     'header': 'https://pdx.social/headers/original/missing.png',
                     'header_static': 'https://pdx.social/headers/original/missing.png',
                     'id': '6717',
                     'locked': True,
                     'note': '<p></p>',
                     'statuses_count': 46,
                     'url': 'https://pdx.social/@moatest',
                     'username': 'moatest'},
         'application': None,
         'content': '<p>RT <span class="h-card"><a href="https://pdx.social/@foozmeat" '
                    'class="u-url mention">@<span>foozmeat</span></a></span> Redis was '
                    'a real a-hole today. I&apos;m sad that we rely on it for job '
                    'queues.</p>',
         'created_at': datetime.datetime(2017, 11, 9, 3, 10, 4, 769000, tzinfo=tzutc()),
         'emojis': [],
         'favourited': False,
         'favourites_count': 0,
         'id': '98972270904179914',
         'in_reply_to_account_id': None,
         'in_reply_to_id': None,
         'language': None,
         'media_attachments': [],
         'mentions': [],
         'muted': False,
         'reblog': {'account': {'acct': 'foozmeat',
                                'avatar': 'https://pdx.social/system/accounts/avatars/000/000/002/original/24f16486ab450a5d.jpg',
                                'avatar_static': 'https://pdx.social/system/accounts/avatars/000/000/002/original/24f16486ab450a5d.jpg',
                                'created_at': datetime.datetime(2017, 4, 7, 1, 22, 15, 768000, tzinfo=tzutc()),
                                'display_name': 'James ✅🚴🐝🍔🕹',
                                'followers_count': 76,
                                'following_count': 143,
                                'header': 'https://pdx.social/system/accounts/headers/000/000/002/original/02d1dd7071e52079.png',
                                'header_static': 'https://pdx.social/system/accounts/headers/000/000/002/original/02d1dd7071e52079.png',
                                'id': '2',
                                'locked': False,
                                'note': '<p>DevOps at Panic. Admin of pdx.social</p>',
                                'statuses_count': 232,
                                'url': 'https://pdx.social/@foozmeat',
                                'username': 'foozmeat'},
                    'application': {'name': 'Web', 'website': None},
                    'content': '<p>Redis was a real a-hole today. I&apos;m sad that we '
                               'rely on it for job queues.</p>',
                    'created_at': datetime.datetime(2017, 11, 8, 0, 29, 53, 970000, tzinfo=tzutc()),
                    'emojis': [],
                    'favourited': False,
                    'favourites_count': 1,
                    'id': '98965978733093918',
                    'in_reply_to_account_id': None,
                    'in_reply_to_id': None,
                    'language': 'en',
                    'media_attachments': [],
                    'mentions': [],
                    'muted': False,
                    'reblog': None,
                    'reblogged': True,
                    'reblogs_count': 1,
                    'sensitive': False,
                    'spoiler_text': '',
                    'tags': [],
                    'uri': 'https://pdx.social/users/foozmeat/statuses/98965978733093918',
                    'url': 'https://pdx.social/@foozmeat/98965978733093918',
                    'visibility': 'public'},
         'reblogged': False,
         'reblogs_count': 0,
         'sensitive': False,
         'spoiler_text': '',
         'tags': [],
         'uri': 'https://pdx.social/users/moatest/statuses/98972270904179914/activity',
         'url': 'https://pdx.social/@moatest/98972270904179914',
         'visibility': 'public'}

boost_w_attachments = {'_pagination_prev': {'_pagination_endpoint': '/api/v1/accounts/6717/statuses',
                                            '_pagination_method': 'GET',
                                            'since_id': 98972419237345529},
                       'account': {'acct': 'moatest',
                                   'avatar': 'https://pdx.social/avatars/original/missing.png',
                                   'avatar_static': 'https://pdx.social/avatars/original/missing.png',
                                   'created_at': datetime.datetime(2017, 10, 30, 20, 34, 29, 216000, tzinfo=tzutc()),
                                   'display_name': '',
                                   'followers_count': 0,
                                   'following_count': 2,
                                   'header': 'https://pdx.social/headers/original/missing.png',
                                   'header_static': 'https://pdx.social/headers/original/missing.png',
                                   'id': '6717',
                                   'locked': True,
                                   'note': '<p></p>',
                                   'statuses_count': 47,
                                   'url': 'https://pdx.social/@moatest',
                                   'username': 'moatest'},
                       'application': None,
                       'content': '<p>RT <span class="h-card"><a href="https://pdx.social/@foozmeat" '
                                  'class="u-url mention">@<span>foozmeat</span></a></span> Finally '
                                  'able to eat the dog food <a '
                                  'href="https://pdx.social/media/72JR2KtOOkFy8S8a7Rw" rel="nofollow '
                                  'noopener" target="_blank"><span '
                                  'class="invisible">https://</span><span '
                                  'class="ellipsis">pdx.social/media/72JR2KtOOkFy8</span><span '
                                  'class="invisible">S8a7Rw</span></a></p>',
                       'created_at': datetime.datetime(2017, 11, 9, 3, 47, 48, 153000, tzinfo=tzutc()),
                       'emojis': [],
                       'favourited': False,
                       'favourites_count': 0,
                       'id': '98972419237345529',
                       'in_reply_to_account_id': None,
                       'in_reply_to_id': None,
                       'language': None,
                       'media_attachments': [],
                       'mentions': [],
                       'muted': False,
                       'reblog': {'account': {'acct': 'foozmeat',
                                              'avatar': 'https://pdx.social/system/accounts/avatars/000/000/002/original/24f16486ab450a5d.jpg',
                                              'avatar_static': 'https://pdx.social/system/accounts/avatars/000/000/002/original/24f16486ab450a5d.jpg',
                                              'created_at': datetime.datetime(2017, 4, 7, 1, 22, 15, 768000,
                                                                              tzinfo=tzutc()),
                                              'display_name': 'James ✅🚴🐝🍔🕹',
                                              'followers_count': 76,
                                              'following_count': 143,
                                              'header': 'https://pdx.social/system/accounts/headers/000/000/002/original/02d1dd7071e52079.png',
                                              'header_static': 'https://pdx.social/system/accounts/headers/000/000/002/original/02d1dd7071e52079.png',
                                              'id': '2',
                                              'locked': False,
                                              'note': '<p>DevOps at Panic. Admin of pdx.social</p>',
                                              'statuses_count': 232,
                                              'url': 'https://pdx.social/@foozmeat',
                                              'username': 'foozmeat'},
                                  'application': {'name': 'Web', 'website': None},
                                  'content': '<p>Finally able to eat the dog food <a '
                                             'href="https://pdx.social/media/72JR2KtOOkFy8S8a7Rw" '
                                             'rel="nofollow noopener" target="_blank"><span '
                                             'class="invisible">https://</span><span '
                                             'class="ellipsis">pdx.social/media/72JR2KtOOkFy8</span><span '
                                             'class="invisible">S8a7Rw</span></a></p>',
                                  'created_at': datetime.datetime(2017, 11, 5, 4, 37, 55, 975000, tzinfo=tzutc()),
                                  'emojis': [],
                                  'favourited': False,
                                  'favourites_count': 0,
                                  'id': '98949967114668601',
                                  'in_reply_to_account_id': None,
                                  'in_reply_to_id': None,
                                  'language': 'en',
                                  'media_attachments': [{'description': 'screenshots',
                                                         'id': '22860',
                                                         'meta': {'original': {'aspect': 1.124780316344464,
                                                                               'height': 1138,
                                                                               'size': '1280x1138',
                                                                               'width': 1280},
                                                                  'small': {'aspect': 1.1235955056179776,
                                                                            'height': 356,
                                                                            'size': '400x356',
                                                                            'width': 400}},
                                                         'preview_url': 'https://pdx.social/system/media_attachments/files/000/022/860/small/aa01670afb664f6f.png',
                                                         'remote_url': None,
                                                         'text_url': 'https://pdx.social/media/72JR2KtOOkFy8S8a7Rw',
                                                         'type': 'image',
                                                         'url': 'https://pdx.social/system/media_attachments/files/000/022/860/original/aa01670afb664f6f.png'}],
                                  'mentions': [],
                                  'muted': False,
                                  'reblog': None,
                                  'reblogged': True,
                                  'reblogs_count': 1,
                                  'sensitive': False,
                                  'spoiler_text': '',
                                  'tags': [],
                                  'uri': 'https://pdx.social/users/foozmeat/statuses/98949967114668601',
                                  'url': 'https://pdx.social/@foozmeat/98949967114668601',
                                  'visibility': 'public'},
                       'reblogged': False,
                       'reblogs_count': 0,
                       'sensitive': False,
                       'spoiler_text': '',
                       'tags': [],
                       'uri': 'https://pdx.social/users/moatest/statuses/98972419237345529/activity',
                       'url': 'https://pdx.social/@moatest/98972419237345529',
                       'visibility': 'public'}

reply1 = {'account': {'acct': 'moatest',
                      'avatar': 'https://pdx.social/avatars/original/missing.png',
                      'avatar_static': 'https://pdx.social/avatars/original/missing.png',
                      'created_at': datetime.datetime(2017, 10, 30, 20, 34, 29, 216000, tzinfo=tzutc()),
                      'display_name': '',
                      'followers_count': 0,
                      'following_count': 2,
                      'header': 'https://pdx.social/headers/original/missing.png',
                      'header_static': 'https://pdx.social/headers/original/missing.png',
                      'id': '6717',
                      'locked': True,
                      'note': '<p></p>',
                      'statuses_count': 49,
                      'url': 'https://pdx.social/@moatest',
                      'username': 'moatest'},
          'application': {'name': 'Web', 'website': None},
          'content': '<p>Reply test 1</p>',
          'created_at': datetime.datetime(2017, 11, 9, 5, 5, 25, 247000, tzinfo=tzutc()),
          'emojis': [],
          'favourited': False,
          'favourites_count': 0,
          'id': '98972724443462491',
          'in_reply_to_account_id': None,
          'in_reply_to_id': None,
          'language': 'en',
          'media_attachments': [],
          'mentions': [],
          'muted': False,
          'reblog': None,
          'reblogged': False,
          'reblogs_count': 0,
          'sensitive': False,
          'spoiler_text': '',
          'tags': [],
          'uri': 'https://pdx.social/users/moatest/statuses/98972724443462491',
          'url': 'https://pdx.social/@moatest/98972724443462491',
          'visibility': 'private'}

reply2 = {'_pagination_prev': {'_pagination_endpoint': '/api/v1/accounts/6717/statuses',
                               '_pagination_method': 'GET',
                               'since_id': 98972725118239719},
          'account': {'acct': 'moatest',
                      'avatar': 'https://pdx.social/avatars/original/missing.png',
                      'avatar_static': 'https://pdx.social/avatars/original/missing.png',
                      'created_at': datetime.datetime(2017, 10, 30, 20, 34, 29, 216000, tzinfo=tzutc()),
                      'display_name': '',
                      'followers_count': 0,
                      'following_count': 2,
                      'header': 'https://pdx.social/headers/original/missing.png',
                      'header_static': 'https://pdx.social/headers/original/missing.png',
                      'id': '6717',
                      'locked': True,
                      'note': '<p></p>',
                      'statuses_count': 49,
                      'url': 'https://pdx.social/@moatest',
                      'username': 'moatest'},
          'application': {'name': 'Web', 'website': None},
          'content': '<p>Reply test 2</p>',
          'created_at': datetime.datetime(2017, 11, 9, 5, 5, 35, 527000, tzinfo=tzutc()),
          'emojis': [],
          'favourited': False,
          'favourites_count': 0,
          'id': '98972725118239719',
          'in_reply_to_account_id': '6717',
          'in_reply_to_id': '98972724443462491',
          'language': 'en',
          'media_attachments': [],
          'mentions': [],
          'muted': False,
          'reblog': None,
          'reblogged': False,
          'reblogs_count': 0,
          'sensitive': False,
          'spoiler_text': '',
          'tags': [],
          'uri': 'https://pdx.social/users/moatest/statuses/98972725118239719',
          'url': 'https://pdx.social/@moatest/98972725118239719',
          'visibility': 'private'}

twitter_mention = {'_pagination_prev': {'_pagination_endpoint': '/api/v1/accounts/6717/statuses',
                                        '_pagination_method': 'GET',
                                        'since_id': 98972792561915550},
                   'account': {'acct': 'moatest',
                               'avatar': 'https://pdx.social/avatars/original/missing.png',
                               'avatar_static': 'https://pdx.social/avatars/original/missing.png',
                               'created_at': datetime.datetime(2017, 10, 30, 20, 34, 29, 216000, tzinfo=tzutc()),
                               'display_name': '',
                               'followers_count': 0,
                               'following_count': 2,
                               'header': 'https://pdx.social/headers/original/missing.png',
                               'header_static': 'https://pdx.social/headers/original/missing.png',
                               'id': '6717',
                               'locked': True,
                               'note': '<p></p>',
                               'statuses_count': 51,
                               'url': 'https://pdx.social/@moatest',
                               'username': 'moatest'},
                   'application': {'name': 'Web', 'website': None},
                   'content': '<p>mentioning @foozmeat@twitter.com here</p>',
                   'created_at': datetime.datetime(2017, 11, 9, 5, 22, 44, 643000, tzinfo=tzutc()),
                   'emojis': [],
                   'favourited': False,
                   'favourites_count': 0,
                   'id': '98972792561915550',
                   'in_reply_to_account_id': None,
                   'in_reply_to_id': None,
                   'language': 'en',
                   'media_attachments': [],
                   'mentions': [],
                   'muted': False,
                   'pinned': False,
                   'reblog': None,
                   'reblogged': False,
                   'reblogs_count': 0,
                   'sensitive': False,
                   'spoiler_text': '',
                   'tags': [],
                   'uri': 'https://pdx.social/users/moatest/statuses/98972792561915550',
                   'url': 'https://pdx.social/@moatest/98972792561915550',
                   'visibility': 'public'}

image_with_description = {'_pagination_prev': {'_pagination_endpoint': '/api/v1/accounts/6717/statuses',
                                               '_pagination_method': 'GET',
                                               'since_id': 98972910281369162},
                          'account': {'acct': 'moatest',
                                      'avatar': 'https://pdx.social/avatars/original/missing.png',
                                      'avatar_static': 'https://pdx.social/avatars/original/missing.png',
                                      'created_at': datetime.datetime(2017, 10, 30, 20, 34, 29, 216000, tzinfo=tzutc()),
                                      'display_name': '',
                                      'followers_count': 0,
                                      'following_count': 2,
                                      'header': 'https://pdx.social/headers/original/missing.png',
                                      'header_static': 'https://pdx.social/headers/original/missing.png',
                                      'id': '6717',
                                      'locked': True,
                                      'note': '<p></p>',
                                      'statuses_count': 54,
                                      'url': 'https://pdx.social/@moatest',
                                      'username': 'moatest'},
                          'application': {'name': 'Web', 'website': None},
                          'content': '<p>image description test</p>',
                          'created_at': datetime.datetime(2017, 11, 9, 5, 52, 40, 901000, tzinfo=tzutc()),
                          'emojis': [],
                          'favourited': False,
                          'favourites_count': 0,
                          'id': '98972910281369162',
                          'in_reply_to_account_id': None,
                          'in_reply_to_id': None,
                          'language': 'fr',
                          'media_attachments': [{'description': 'gitlab logo',
                                                 'id': '24511',
                                                 'meta': {'original': {'aspect': 1.0,
                                                                       'height': 500,
                                                                       'size': '500x500',
                                                                       'width': 500},
                                                          'small': {'aspect': 1.0,
                                                                    'height': 400,
                                                                    'size': '400x400',
                                                                    'width': 400}},
                                                 'preview_url': 'https://pdx.social/system/media_attachments/files/000/024/511/small/c22299c464a7d72f.png',
                                                 'remote_url': None,
                                                 'text_url': 'https://pdx.social/media/kVwpv8trzfEgOg8iOPI',
                                                 'type': 'image',
                                                 'url': 'https://pdx.social/system/media_attachments/files/000/024/511/original/c22299c464a7d72f.png'}],
                          'mentions': [],
                          'muted': False,
                          'reblog': None,
                          'reblogged': False,
                          'reblogs_count': 0,
                          'sensitive': False,
                          'spoiler_text': '',
                          'tags': [],
                          'uri': 'https://pdx.social/users/moatest/statuses/98972910281369162',
                          'url': 'https://pdx.social/@moatest/98972910281369162',
                          'visibility': 'private'}

toot_with_mention = {'_pagination_prev': {'_pagination_endpoint': '/api/v1/accounts/6717/statuses',
                                          '_pagination_method': 'GET',
                                          'since_id': 98976347364553358},
                     'account': {'acct': 'moatest',
                                 'avatar': 'https://pdx.social/avatars/original/missing.png',
                                 'avatar_static': 'https://pdx.social/avatars/original/missing.png',
                                 'created_at': datetime.datetime(2017, 10, 30, 20, 34, 29, 216000, tzinfo=tzutc()),
                                 'display_name': '',
                                 'followers_count': 0,
                                 'following_count': 2,
                                 'header': 'https://pdx.social/headers/original/missing.png',
                                 'header_static': 'https://pdx.social/headers/original/missing.png',
                                 'id': '6717',
                                 'locked': True,
                                 'note': '<p></p>',
                                 'statuses_count': 58,
                                 'url': 'https://pdx.social/@moatest',
                                 'username': 'moatest'},
                     'application': {'name': 'Web', 'website': None},
                     'content': '<p>mentioning <span class="h-card"><a '
                                'href="https://pdx.social/@foozmeat" class="u-url '
                                'mention">@<span>foozmeat</span></a></span> here</p>',
                     'created_at': datetime.datetime(2017, 11, 9, 20, 26, 46, 625000, tzinfo=tzutc()),
                     'emojis': [],
                     'favourited': False,
                     'favourites_count': 0,
                     'id': '98976347364553358',
                     'in_reply_to_account_id': None,
                     'in_reply_to_id': None,
                     'language': 'en',
                     'media_attachments': [],
                     'mentions': [{'acct': 'foozmeat',
                                   'id': '2',
                                   'url': 'https://pdx.social/@foozmeat',
                                   'username': 'foozmeat'}],
                     'muted': False,
                     'reblog': None,
                     'reblogged': False,
                     'reblogs_count': 0,
                     'sensitive': False,
                     'spoiler_text': '',
                     'tags': [],
                     'uri': 'https://pdx.social/users/moatest/statuses/98976347364553358',
                     'url': 'https://pdx.social/@moatest/98976347364553358',
                     'visibility': 'private'}

toot_double_mention = {'_pagination_prev': {'_pagination_endpoint': '/api/v1/accounts/6717/statuses',
                                            '_pagination_method': 'GET',
                                            'since_id': 99078721594621415},
                       'account': {'acct': 'moatest',
                                   'avatar': 'https://pdx.social/avatars/original/missing.png',
                                   'avatar_static': 'https://pdx.social/avatars/original/missing.png',
                                   'created_at': datetime.datetime(2017, 10, 30, 20, 34, 29, 216000, tzinfo=tzutc()),
                                   'display_name': 'Moa test account',
                                   'followers_count': 0,
                                   'following_count': 1,
                                   'header': 'https://pdx.social/headers/original/missing.png',
                                   'header_static': 'https://pdx.social/headers/original/missing.png',
                                   'id': 6717,
                                   'locked': True,
                                   'note': '<p>Lot&apos;s of random garbage posts. You should ignore '
                                           'it.</p>',
                                   'statuses_count': 99,
                                   'url': 'https://pdx.social/@moatest',
                                   'username': 'moatest'},
                       'application': {'name': 'Web', 'website': None},
                       'content': '<p>test 1 <span class="h-card"><a '
                                  'href="https://pdx.social/@moa_party" class="u-url '
                                  'mention">@<span>moa_party</span></a></span><br />test 2 '
                                  '@moa_party@twitter.com</p>',
                       'created_at': datetime.datetime(2017, 11, 27, 22, 21, 53, 411000, tzinfo=tzutc()),
                       'emojis': [],
                       'favourited': False,
                       'favourites_count': 0,
                       'id': 99078721594621415,
                       'in_reply_to_account_id': None,
                       'in_reply_to_id': None,
                       'language': 'en',
                       'media_attachments': [],
                       'mentions': [{'acct': 'moa_party',
                                     'id': 8598,
                                     'url': 'https://pdx.social/@moa_party',
                                     'username': 'moa_party'}],
                       'muted': False,
                       'reblog': None,
                       'reblogged': False,
                       'reblogs_count': 0,
                       'sensitive': False,
                       'spoiler_text': '',
                       'tags': [],
                       'uri': 'https://pdx.social/users/moatest/statuses/99078721594621415',
                       'url': 'https://pdx.social/@moatest/99078721594621415',
                       'visibility': 'private'}

toot_with_cw = {'_pagination_prev': {'_pagination_endpoint': '/api/v1/accounts/6717/statuses',
                                     '_pagination_method': 'GET',
                                     'since_id': 99079553123383380},
                'account': {'acct': 'moatest',
                            'avatar': 'https://pdx.social/avatars/original/missing.png',
                            'avatar_static': 'https://pdx.social/avatars/original/missing.png',
                            'created_at': datetime.datetime(2017, 10, 30, 20, 34, 29, 216000, tzinfo=tzutc()),
                            'display_name': 'Moa test account',
                            'followers_count': 0,
                            'following_count': 1,
                            'header': 'https://pdx.social/headers/original/missing.png',
                            'header_static': 'https://pdx.social/headers/original/missing.png',
                            'id': 6717,
                            'locked': True,
                            'note': '<p>Lot&apos;s of random garbage posts. You should ignore '
                                    'it.</p>',
                            'statuses_count': 104,
                            'url': 'https://pdx.social/@moatest',
                            'username': 'moatest'},
                'application': {'name': 'Web', 'website': None},
                'content': '<p>This is the secret stuff</p>',
                'created_at': datetime.datetime(2017, 11, 28, 1, 53, 21, 534000, tzinfo=tzutc()),
                'emojis': [],
                'favourited': False,
                'favourites_count': 0,
                'id': 99079553123383380,
                'in_reply_to_account_id': None,
                'in_reply_to_id': None,
                'language': 'en',
                'media_attachments': [],
                'mentions': [],
                'muted': False,
                'reblog': None,
                'reblogged': False,
                'reblogs_count': 0,
                'sensitive': True,
                'spoiler_text': 'This is the spoiler text',
                'tags': [],
                'uri': 'https://pdx.social/users/moatest/statuses/99079553123383380',
                'url': 'https://pdx.social/@moatest/99079553123383380',
                'visibility': 'private'}

toot_with_many_urls = {'_pagination_prev': {'_pagination_endpoint': '/api/v1/accounts/12083/statuses',
                                            '_pagination_method': 'GET',
                                            'since_id': 99113667863200595},
                       'account': {'acct': 'kacealexander',
                                   'avatar': 'https://wandering.shop/system/accounts/avatars/000/012/083/original/7b7daab1234cede81647d4aeb039a7e3.png',
                                   'avatar_static': 'https://wandering.shop/system/accounts/avatars/000/012/083/original/7b7daab1234cede81647d4aeb039a7e3.png',
                                   'created_at': datetime.datetime(2017, 11, 13, 20, 43, 54, 343000, tzinfo=tzutc()),
                                   'display_name': 'K. C. Alexander',
                                   'followers_count': 130,
                                   'following_count': 54,
                                   'header': 'https://wandering.shop/system/accounts/headers/000/012/083/original/50bdde4d0e78a313d903e81d750dc330.png',
                                   'header_static': 'https://wandering.shop/system/accounts/headers/000/012/083/original/50bdde4d0e78a313d903e81d750dc330.png',
                                   'id': 12083,
                                   'locked': False,
                                   'note': '<p>Author. Transhumanism and profanity. She/they/just '
                                           'this guy, you know? Never knows where the towels are at. '
                                           '</p><p>www.kcalexander.com</p>',
                                   'statuses_count': 392,
                                   'url': 'https://wandering.shop/@kacealexander',
                                   'username': 'kacealexander'},
                       'application': None,
                       'content': '<p>Goddamn, I love mastodon, y&apos;all. Please come join it. '
                                  'wandering.shop is where a lot of your fave authors are gathering, '
                                  'and mastodon.social is a good place, too. But don&apos;t let '
                                  'those two stop you. There are many instances (like scifi.fyi or '
                                  'witches.town or... joinmastodon.com)</p><p>I&apos;m really '
                                  'content here.</p>',
                       'created_at': datetime.datetime(2017, 12, 4, 2, 29, 11, 272000, tzinfo=tzutc()),
                       'emojis': [],
                       'favourited': False,
                       'favourites_count': 1,
                       'id': 99113667863200595,
                       'in_reply_to_account_id': None,
                       'in_reply_to_id': None,
                       'language': 'en',
                       'media_attachments': [],
                       'mentions': [],
                       'muted': False,
                       'pinned': False,
                       'reblog': None,
                       'reblogged': False,
                       'reblogs_count': 0,
                       'sensitive': False,
                       'spoiler_text': '',
                       'tags': [],
                       'uri': 'https://wandering.shop/users/kacealexander/statuses/99113667863200595',
                       'url': 'https://wandering.shop/@kacealexander/99113667863200595',
                       'visibility': 'public'}
