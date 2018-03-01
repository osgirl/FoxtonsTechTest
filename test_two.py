import requests

class Album():

    url = 'https://jsonplaceholder.typicode.com/albums'
    json_object = ''

    def counter_user_occurence(self, userid):
        return len([x for x in self.json_object if x['userId'] == userid])

    def counter_distinct_users(self):
        return len(set([x['userId'] for x in self.json_object]))

    def longest_album(self):
        return max([x['title'] for x in self.json_object], key=len)

if __name__ == '__main__':
    album = Album()
    album.json_object = requests.get(album.url).json()
    print ("this user shows up {} times".format(album.counter_user_occurence(1)))
    print ("there are {} distinct users".format(album.counter_distinct_users()))
    print ("the longest title is {}".format(album.longest_album()))