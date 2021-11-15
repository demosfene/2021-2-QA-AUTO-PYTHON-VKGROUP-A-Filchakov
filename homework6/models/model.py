from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CountRequest(Base):
    __tablename__ = 'count_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<count_requests(" \
               f"id='{self.id}'," \
               f"requests_count='{self.requests_count}', " \
               f")>\n"

    id = Column(Integer, primary_key=True, autoincrement=True)
    requests_count = Column(Integer, nullable=False)


class CountRequestByType(Base):
    __tablename__ = 'count_request_of_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<count_request_of_type(" \
               f"id='{self.id}'," \
               f"type='{self.type}', " \
               f"requests_count='{self.requests_count}'" \
               f")>\n"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(300), nullable=False)
    requests_count = Column(Integer, nullable=False)


class CountRequestByUrl(Base):
    __tablename__ = 'count_request_of_url'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<count_request_of_url(" \
               f"id='{self.id}'," \
               f"urls='{self.urls}', " \
               f"requests_count='{self.requests_count}'" \
               f")>\n"

    id = Column(Integer, primary_key=True, autoincrement=True)
    urls = Column(String(300), nullable=False)
    requests_count = Column(Integer, nullable=False)


class CountRequestByLength4xx(Base):
    __tablename__ = 'count_request_of_length_4xx'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<count_request_of_length_4xx(" \
               f"id='{self.id}'," \
               f"urls='{self.urls}', " \
               f"status_code='{self.status_code}'" \
               f"length='{self.length}'" \
               f"ip='{self.ip}'" \
               f")>\n"

    id = Column(Integer, primary_key=True, autoincrement=True)
    urls = Column(String(300), nullable=False)
    status_code = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    ip = Column(String(90), nullable=False)


class CountRequestByUsers5xx(Base):
    __tablename__ = 'count_request_of_users_5xx'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<count_request_of_length_4xx(" \
               f"id='{self.id}'," \
               f"ip='{self.ip}', " \
               f"requests_count='{self.requests_count}'" \
               f")>\n"

    id = Column(Integer, primary_key=True, autoincrement=True)
    requests_count = Column(Integer, nullable=False)
    ip = Column(String(90), nullable=False)
