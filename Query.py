from mal import *
from mal import Manga
from mal import MangaSearch
from mal import AnimeSearch

class QueryTestCase:
    def __init__(self, search : str , u_episodes : int , u_volumes : int):
        self.search = search
        self.u_episodes = u_episodes
        self.u_volumes = u_volumes       
        self.mal_AnimeID = AnimeSearch(self.search).results[0].mal_id
        self.a_episodes = Anime(self.mal_AnimeID).episodes
        self.mal_MangaID = MangaSearch(self.search).results[0].mal_id
        self.m_volumes = Manga(self.mal_MangaID).volumes
    def EpisodesLeft(self):
        if self.a_episodes == None:
            return f'{self.search} is still ongoing!'
        elif self.u_episodes < self.a_episodes and self.a_episodes != None:
            return self.a_episodes - self.u_episodes
        elif self.u_episodes > self.a_episodes:
            return f'you have completed the show {self.search}!'
    def Volumesleft(self):
        if self.m_volumes == None:
            return f'{self.search} is still ongoing!'
        elif self.u_volumes < self.m_volumes and self.m_volumes != None:
            return self.m_volumes - self.u_volumes
        elif self.u_episodes > self.m_volumes:
            return f'you have completed the show {self.search}!' 


