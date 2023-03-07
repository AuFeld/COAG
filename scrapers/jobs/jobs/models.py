from typing import Optional
from pydantic import BaseModel, Field, HttpUrl

class Board(BaseModel): 
    '''
    Job board jobs were scraped from 
    '''
    title: Optional[str] = Field(...) 
    slug: Optional[str] = Field(...)
    url: Optional[HttpUrl] = Field(...)

    class Meta: 
        ''' 
        Order by title
        '''
        ordering = ['title']

    def __str__(self):
        '''
        Set title
        '''
        return f'{self.title}'

class Company(BaseModel): 
    title: Optional[str] = Field(...) 
    slug: Optional[str] = Field(...)
    email: Optional[str] = Field(...)
    url: Optional[HttpUrl] = Field(...)
    about: Optional[str] = Field(...)

    class Meta:
        '''
        Order by title
        '''
        ordering = ['title']
    
    def __str__(self):
        '''
        Set title
        '''
        return f'{self.title}'

class Job(BaseModel):
    title: Optional[str] = Field(...)
    board: Optional[str] = Field(...)
    company: Optional[str] = Field(...)
    url: Optional[HttpUrl] = Field(...)
    pub_date: Optional[str] = Field(...)
    scrape_date: Optional[str] = Field(...)
    location: Optional[str] = Field(...)

    class Meta:
        '''
        order by scrape date
        '''
        ordering = ['scrape_date']
    
    def __str__(self):
        '''
        Set title
        '''
        return f'{self.title}'

    def short_url(self):
        '''
        Return a clickable link
        '''
        if self.url: 
            return f'<a href="{self.url}">{self.title}</a>'
        else:
            return self.url
        
    def get_count(self):
        '''
        Return total number of jobs
        '''
        return self.objects.all().count()


class SearchTerms(BaseModel): 
    term: Optional[str] = Field(...)

    def __str__(self):
        '''
        Set title
        '''
        return f'{self.term}'

class Tag(BaseModel): 
    tag: Optional[str] = Field(...)
    job: Optional[str] = Field(...)
