import requests, threading, json, random, time

proxies = []


message = json.loads(open('content\\config.json', 'r').read())['message']

cookies = open('content\\cookies.txt', 'r').read().splitlines()


def sendMessage(cookie):
    global proxies
    with requests.session() as session:
        session.cookies['.ROBLOSECURITY'] = cookie

        session.headers['x-csrf-token'] = session.post(
            'https://friends.roblox.com/v1/users/1/request-friendship',

            data = {}

        ).headers['x-csrf-token']

        selfUserId = session.get(
            'https://users.roblox.com/v1/users/authenticated'
        ).json()[
            'id'
        ]

        friends = session.get(
            f'https://friends.roblox.com/v1/users/{selfUserId}/friends?userSort=StatusAlphabetical'
        ).json()[
            'data'
        ]
        
        for user in friends:
            time.sleep(3)
            try:
                friendId = user['id']
                convId = session.post(
                    'https://chat.roblox.com/v2/start-one-to-one-conversation',

                    data = {
                        'participantUserId':friendId
                    }
                ).json()['conversation']['id']

                sendMSG = session.post(
                    'https://chat.roblox.com/v2/send-message',

                    data = {
                        'conversationId':convId,

                        'message':message
                    }
                )
                print ( sendMSG.text )
            except:
                print('-> There was an error while trying to process!')

for x in cookies:

    threading.Thread(target=sendMessage, args=(x,)).start()

input()