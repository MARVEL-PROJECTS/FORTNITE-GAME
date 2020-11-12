from pfaw import Fortnite, Platform, Mode

fortnite = Fortnite(fortnite_token='FORTNITE_TOKEN', launcher_token='LAUNCHER_TOKEN',
                    password='PASSWORD', email='EMAIL')
                    player = fortnite.player(username='tejaaaki')

print(player.name)
print(player.id)

# prints:
# tejaaaki
# 9c9212603304472d831c03d0978d2bc1
stats = fortnite.battle_royale_stats(username='tejaaaki', platform=Platform.pc)

print(f'Solo Wins: {stats.solo.wins}')
print(f'Duo Wins: {stats.duo.wins}')
print(f'Squad Wins: {stats.squad.wins}')
print(f'Lifetime Wins: {stats.all.wins}')


# prints:
# Solo Wins: 1051
# Duo Wins: 1005
# Squad Wins: 210
# Lifetime Wins: 2266
status = fortnite.server_status()

if status:
    print('Servers are UP!')
else:
    print('Servers are DOWN.')
smittys_pals = fortnite.friends(username='Smitty Werbenjagermanjensen')

for friend in smittys_pals:
    print(friend)
    news = fortnite.news()

for br_news in news.br:
    print(br_news.image)
    print(br_news.title)
    print(br_news.body)
    store = fortnite.store()

print(store.refresh_interval_hrs)
print(store.daily_purchase_hrs)
print(store.expiration)

for front in store.storefronts:
    print(front.name)

    for entry in front.catalog_entries:
        print(entry.offer_id)
        print(entry.dev_name)
        print(entry.offer_type)
        print(entry.title)
        print(entry.description)
        print(entry.refundable)

        for price in entry.prices:
            print(price.currency_type)
            print(price.regular_price)
            print(price.final_price)
            print(price.sale_expiration)
            print(price.base_price)
            leaderboard = fortnite.leaderboard(count=10, platform=Platform.pc, mode=Mode.solo)

for player in leaderboard:
    print(f'{player.id} - {player.name} - {player.rank} - {player.value}')

# prints:
# 385c4d9ab7e3498db533ff4d2d9f4c5b - twitch_bogdanakh - 1 - 909
# 155234bbadaa4e8199a7b2d413722290 - TwitchTV.lavak3_ - 2 - 805
# c083d2200d654b25a87c0c48cb76c902 - Agares29_Twitch - 3 - 781
# 0041d08bedc548d9a2230c4a28550594 - Myboosting.com2 - 4 - 736
# 6f5c77adef1c4e47bc33f1f0c8b4b263 - Twitch_DutchHawk - 5 - 728
# e94c3e05284443398803285171550b45 - twitchtvLIKANDOO - 6 - 675
# 13b3c77420da4101a213e1f646b316a9 - Twitch APEXENITH - 7 - 675
# b94176db4c254f9099fb2bd8e8ae0f94 - VaxitylolMIXERtv - 8 - 624
# cfd16ec54126497ca57485c1ee1987dc - SypherPK - 9 - 608
# a9467569462d4149bc438550c03a45c9 - RuralKTmixer.com - 10 - 607
