import facebook
import requests

def feed():
    app_id = '551303715627319'
    app_secret = '253b1045c14151df9f5b679db9edfc96'
    user_short_token = 'EAAH1aGYiITcBAP0i1ZCtjWB9CVqaDL7kTIxZCgnOnjAyXlFMnCtzOcwgzhWXpuYGVRofgu1II9ap324zBDiBH1X59ZAYOlRLjTI7Rijw97Ok6d9OPiOpBwwp8TKOrZB2apYbXBZBbYiAoi0TfCPZCoZC3JMMZADmHkthNXZCUpXrBXgZDZD'
    access_token_url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}'.format(app_id, app_secret, user_short_token)
    r = requests.get(access_token_url)
    access_token_info = r.json()
    user_long_token = access_token_info['access_token']
    graph = facebook.GraphAPI(access_token = user_long_token, version = '3.0')
    pages_data = graph.get_object(id = "887065461390197", fields = 'feed')
    a = pages_data['feed']['data']
    id = a[0]['id']
    post_id = id.split('_')

    # посилання, лінк інколи глючить
    try:
        link1 = graph.get_object(id = id, fields = 'link')
        if link1['link'].index('google'):
            link = "\nПосилання:\n" + link1['link']
        elif link1['link'].index('impuls'):
            link = ''
    except:
        link = ''

    try:
        url1 = graph.get_object(id = id, fields = 'attachments')
        if url1['attachments']['data'][0]['type'] == 'video_inline':
            url = '\nВідео: \n' + url1['attachments']['data'][0]['url']
        else:
            url = ''
    except:
        url = ''

    #спроба отримати пости
    try:
        post2 = graph.get_object(id = id, fields = 'message')
        try:
            post1 = graph.get_object(id = id, fields = 'description')
            post = post2['message'] + '\n' + post1['description'] + url + link
            print(post)
            if post.find('ПРЕС'):
                post = post[:post.find('ПРЕС')] + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            else:
                post = post + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            print(post)
        except:
            post = post2['message'] + url + link
            print(post)
            if post.find('ПРЕС'):
                post = post[:post.find('ПРЕС')] + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            else:
                post = post + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            print(post)
    except:
        try:
            post1 = graph.get_object(id = id, fields = 'description')
            post = post1['description'] + url + link
            print(post)
            if post.find('ПРЕС'):
                post = post[:post.find('ПРЕС')] + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            else:
                post = post + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            print(post)
        except:
            post = '\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]

    arr_photo = []
    try:
        src = graph.get_object(id = id, fields = 'attachments')
        # if src['attachments']['data'][0]['media']['image']['width'] > 100 or src['attachments']['data'][0]['subattachments']['data'][0]['media']['image']['width'] > 100:
        try:
            for i in range(len(src['attachments']['data'])):
                arr_photo.append(src['attachments']['data'][0]['media']['image']['src'])
        except:
            try:
                for i in range(len(src['attachments']['data'][0]['subattachments']['data'])):
                    arr_photo.append(src['attachments']['data'][0]['subattachments']['data'][i]['media']['image']['src'])
            except:
                arr_photo.append('https://scontent.fiev25-2.fna.fbcdn.net/v/t1.0-9/78906943_519876088598038_7519946367553241088_n.jpg?_nc_cat=110&_nc_ohc=8IfubHYd1EsAQkVBzTWB2k3EiFZX0tyO_E8OPeXIFOLuF1Gaia4SxRXKA&_nc_ht=scontent.fiev25-2.fna&oh=1c4962f18b6c8ccf49785e7984eabf5b&oe=5E7723B2')
        # else:
            # arr_photo.append('https://scontent.fiev25-2.fna.fbcdn.net/v/t1.0-9/78906943_519876088598038_7519946367553241088_n.jpg?_nc_cat=110&_nc_ohc=8IfubHYd1EsAQkVBzTWB2k3EiFZX0tyO_E8OPeXIFOLuF1Gaia4SxRXKA&_nc_ht=scontent.fiev25-2.fna&oh=1c4962f18b6c8ccf49785e7984eabf5b&oe=5E7723B2')
    except:
            arr_photo.append('https://scontent.fiev25-2.fna.fbcdn.net/v/t1.0-9/78906943_519876088598038_7519946367553241088_n.jpg?_nc_cat=110&_nc_ohc=8IfubHYd1EsAQkVBzTWB2k3EiFZX0tyO_E8OPeXIFOLuF1Gaia4SxRXKA&_nc_ht=scontent.fiev25-2.fna&oh=1c4962f18b6c8ccf49785e7984eabf5b&oe=5E7723B2')
    return post, arr_photo

def feed_1():
    app_id = '416980588924278'
    app_secret = 'b7cd36cb4dd99deeb6fe34ad3b412177'
    user_short_token = 'EAAF7PdvhjXYBAAKFZBvlAK7IO9qtvpBYNw4jGbZA6tliIdHMR6qKL0Atpt3bHSDHmCDjyodSdkXZAmNZAwIBqFczMrZBpX6XxCFIybX3FZAo1NzxmqhX4CtjJE1iIhtkznOvZAJ4Yx7lE01BjB4POGlWmBO7ZCvH66u7ZCkoUDzy7UQZDZD'
    access_token_url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}'.format(app_id, app_secret, user_short_token)
    r = requests.get(access_token_url)
    access_token_info = r.json()
    user_long_token = access_token_info['access_token']
    graph = facebook.GraphAPI(access_token = user_long_token, version = '3.0')
    pages_data = graph.get_object(id = "887065461390197", fields = 'feed')
    a = pages_data['feed']['data']
    id = a[0]['id']
    post_id = id.split('_')

    # посилання, лінк інколи глючить
    try:
        link1 = graph.get_object(id = id, fields = 'link')
        if link1['link'].index('google'):
            link = "\nПосилання:\n" + link1['link']
        elif link1['link'].index('impuls'):
            link = ''
    except:
        link = ''

    try:
        url1 = graph.get_object(id = id, fields = 'attachments')
        if url1['attachments']['data'][0]['type'] == 'video_inline':
            url = '\nВідео: \n' + url1['attachments']['data'][0]['url']
        else:
            url = ''
    except:
        url = ''

    #спроба отримати пости
    try:
        post2 = graph.get_object(id = id, fields = 'message')
        try:
            post1 = graph.get_object(id = id, fields = 'description')
            post = post2['message'] + '\n' + post1['description'] + url + link
            print(post)
            if post.find('ПРЕС'):
                post = post[:post.find('ПРЕС')]+ '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            else:
                post = post + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            print(post)
        except:
            post = post2['message'] + url + link
            print(post)
            if post.find('ПРЕС'):
                post = post[:post.find('ПРЕС')]+ '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            else:
                post = post + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            print(post)
    except:
        try:
            post1 = graph.get_object(id = id, fields = 'description')
            post = post1['description'] + url + link
            print(post)
            if post.find('ПРЕС'):
                post = post[:post.find('ПРЕС')] + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            else:
                post = post + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            print(post)
        except:
            post = '\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]

    arr_photo = []
    try:
        src = graph.get_object(id = id, fields = 'attachments')
        # if src['attachments']['data'][0]['media']['image']['width'] > 100 or src['attachments']['data'][0]['subattachments']['data'][0]['media']['image']['width'] > 100:
        try:
            for i in range(len(src['attachments']['data'])):
                arr_photo.append(src['attachments']['data'][0]['media']['image']['src'])
        except:
            try:
                for i in range(len(src['attachments']['data'][0]['subattachments']['data'])):
                    arr_photo.append(src['attachments']['data'][0]['subattachments']['data'][i]['media']['image']['src'])
            except:
                arr_photo.append('https://scontent.fiev25-2.fna.fbcdn.net/v/t1.0-9/78906943_519876088598038_7519946367553241088_n.jpg?_nc_cat=110&_nc_ohc=8IfubHYd1EsAQkVBzTWB2k3EiFZX0tyO_E8OPeXIFOLuF1Gaia4SxRXKA&_nc_ht=scontent.fiev25-2.fna&oh=1c4962f18b6c8ccf49785e7984eabf5b&oe=5E7723B2')
        # else:
            # arr_photo.append('https://scontent.fiev25-2.fna.fbcdn.net/v/t1.0-9/78906943_519876088598038_7519946367553241088_n.jpg?_nc_cat=110&_nc_ohc=8IfubHYd1EsAQkVBzTWB2k3EiFZX0tyO_E8OPeXIFOLuF1Gaia4SxRXKA&_nc_ht=scontent.fiev25-2.fna&oh=1c4962f18b6c8ccf49785e7984eabf5b&oe=5E7723B2')
    except:
            arr_photo.append('https://scontent.fiev25-2.fna.fbcdn.net/v/t1.0-9/78906943_519876088598038_7519946367553241088_n.jpg?_nc_cat=110&_nc_ohc=8IfubHYd1EsAQkVBzTWB2k3EiFZX0tyO_E8OPeXIFOLuF1Gaia4SxRXKA&_nc_ht=scontent.fiev25-2.fna&oh=1c4962f18b6c8ccf49785e7984eabf5b&oe=5E7723B2')
    return post, arr_photo

def mine():
    app_id = '416980588924278'
    app_secret = 'b7cd36cb4dd99deeb6fe34ad3b412177'
    user_short_token = 'EAAF7PdvhjXYBAAKFZBvlAK7IO9qtvpBYNw4jGbZA6tliIdHMR6qKL0Atpt3bHSDHmCDjyodSdkXZAmNZAwIBqFczMrZBpX6XxCFIybX3FZAo1NzxmqhX4CtjJE1iIhtkznOvZAJ4Yx7lE01BjB4POGlWmBO7ZCvH66u7ZCkoUDzy7UQZDZD'
    access_token_url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}'.format(app_id, app_secret, user_short_token)
    r = requests.get(access_token_url)
    access_token_info = r.json()
    user_long_token = access_token_info['access_token']
    graph = facebook.GraphAPI(access_token = user_long_token, version = '3.0')
    pages_data = graph.get_object(id = "1427279774077251", fields = 'feed')
    a = pages_data['feed']['data']
    id = a[0]['id']
    post_id = id.split('_')

    # посилання, лінк інколи глючить
    try:
        link1 = graph.get_object(id = id, fields = 'link')
        if link1['link'].index('google'):
            link = "\nПосилання:\n" + link1['link']
        elif link1['link'].index('impuls'):
            link = ''
    except:
        link = ''

    try:
        url1 = graph.get_object(id = id, fields = 'attachments')
        if url1['attachments']['data'][0]['type'] == 'video_inline':
            url = '\nВідео: \n' + url1['attachments']['data'][0]['url']
        else:
            url = ''
    except:
        url = ''

    #спроба отримати пости
    try:
        post2 = graph.get_object(id = id, fields = 'message')
        try:
            post1 = graph.get_object(id = id, fields = 'description')
            post = post2['message'] + '\n' + post1['description'] + url + link
            print(post)
            if post.find('ПРЕС'):
                post = post[:post.find('ПРЕС')]+ '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            else:
                post = post + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            print(post)
        except:
            post = post2['message'] + url + link
            print(post)
            if post.find('ПРЕС'):
                post = post[:post.find('ПРЕС')]+ '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            else:
                post = post + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            print(post)
    except:
        try:
            post1 = graph.get_object(id = id, fields = 'description')
            post = post1['description'] + url + link
            print(posy)
            if post.find('ПРЕС'):
                post = post[:post.find('ПРЕС')] + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            else:
                post = post + '\n\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]
            print(post)
        except:
            post = '\nПосилання на Facebook: https://www.facebook.com/' + post_id[0] + '/posts/' + post_id[1]

    arr_photo = []
    try:
        src = graph.get_object(id = id, fields = 'attachments')
        # if src['attachments']['data'][0]['media']['image']['width'] > 100 or src['attachments']['data'][0]['subattachments']['data'][0]['media']['image']['width'] > 100:
        try:
            for i in range(len(src['attachments']['data'])):
                arr_photo.append(src['attachments']['data'][0]['media']['image']['src'])
        except:
            try:
                for i in range(len(src['attachments']['data'][0]['subattachments']['data'])):
                    arr_photo.append(src['attachments']['data'][0]['subattachments']['data'][i]['media']['image']['src'])
            except:
                arr_photo.append('https://scontent.fiev25-2.fna.fbcdn.net/v/t1.0-9/78906943_519876088598038_7519946367553241088_n.jpg?_nc_cat=110&_nc_ohc=8IfubHYd1EsAQkVBzTWB2k3EiFZX0tyO_E8OPeXIFOLuF1Gaia4SxRXKA&_nc_ht=scontent.fiev25-2.fna&oh=1c4962f18b6c8ccf49785e7984eabf5b&oe=5E7723B2')
        # else:
            # arr_photo.append('https://scontent.fiev25-2.fna.fbcdn.net/v/t1.0-9/78906943_519876088598038_7519946367553241088_n.jpg?_nc_cat=110&_nc_ohc=8IfubHYd1EsAQkVBzTWB2k3EiFZX0tyO_E8OPeXIFOLuF1Gaia4SxRXKA&_nc_ht=scontent.fiev25-2.fna&oh=1c4962f18b6c8ccf49785e7984eabf5b&oe=5E7723B2')
    except:
            arr_photo.append('https://scontent.fiev25-2.fna.fbcdn.net/v/t1.0-9/78906943_519876088598038_7519946367553241088_n.jpg?_nc_cat=110&_nc_ohc=8IfubHYd1EsAQkVBzTWB2k3EiFZX0tyO_E8OPeXIFOLuF1Gaia4SxRXKA&_nc_ht=scontent.fiev25-2.fna&oh=1c4962f18b6c8ccf49785e7984eabf5b&oe=5E7723B2')
    return post, arr_photo
