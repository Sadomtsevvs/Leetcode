class Codec:

    mapp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def __init__(self):

        self.id_long = {}
        self.long_id = {}

    def encode(self, longUrl: str) -> str:

        n = self.long_id.get(longUrl)
        if n is None:
            n = len(self.long_id) + 1
            self.id_long[n] = longUrl
            self.long_id[longUrl] = n

        short = ''
        while n > 0:
            a, b = divmod(n, 62)
            short += Codec.mapp[b]
            n = a

        return 'http://tinyurl.com/'+short[::-1]

    def decode(self, shortUrl: str) -> str:

        n = 0

        for char in shortUrl[19:]:
            if 'a' <= char <= 'z':
                n = n * 62 + ord(char) - ord('a')
            elif 'A' <= char <= 'Z':
                n = n * 62 + ord(char) - ord('A') + 26
            else:
                n = n * 62 + ord(char) - ord('0') + 52

        return self.id_long[n]

        # from LC comments
        #
        # class Codec:
        #
        #     alphabet = string.ascii_letters + '0123456789'
        #
        #     def __init__(self):
        #         self.url2code = {}
        #         self.code2url = {}
        #
        #     def encode(self, longUrl):
        #         while longUrl not in self.url2code:
        #             code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
        #             if code not in self.code2url:
        #                 self.code2url[code] = longUrl
        #                 self.url2code[longUrl] = code
        #         return 'http://tinyurl.com/' + self.url2code[longUrl]
        #
        #     def decode(self, shortUrl):
        #         return self.code2url[shortUrl[-6:]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
