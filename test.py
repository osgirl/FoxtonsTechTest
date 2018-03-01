import requests

class Album():

    url = 'https://jsonplaceholder.typicode.com/albums'
    json_object = ''

    def call_api(self):
        self.json_object = requests.get(self.url).json()

    def count_album(self):
        count = 0
        for items in self.json_object:
            userId = items['userId']
            if userId == 2:
                count = count + 1
        print("User 2 has {} albums.".format(count))

    def count_users(self):
        count = 0
        users = []
        for items in self.json_object:
            userId = items['userId']
            if userId not in users:
                users.append(userId)
                count = count + 1
        print("There are {} unique users.".format(count))

    def longest_album(self):
        album_List = []
        for items in self.json_object:
            title = items['title']
            album_List.append(title)
        print(max(album_List,key=len), "is the longest album name.")

if __name__ == '__main__':
    album = Album()
    album.call_api()
    album.count_album()
    album.count_users()
    album.longest_album()



