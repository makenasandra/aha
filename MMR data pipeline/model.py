from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class BodyAccX(Base):
    __tablename__ = 'body_acc_x'
    id = Column(Integer, primary_key=True)
    row_data = Column(String)
    label = Column(String)

    def __repr__(self):
        return self.label


class BodyAccY(Base):
    __tablename__ = 'body_acc_y'
    id = Column(Integer, primary_key=True)
    row_data = Column(String)
    label = Column(String)

    def __repr__(self):
        return self.label


class BodyAccZ(Base):
    __tablename__ = 'body_acc_z'
    id = Column(Integer, primary_key=True)
    row_data = Column(String)
    label = Column(String)

    def __repr__(self):
        return self.label


class BodyGyroX(Base):
    __tablename__ = 'body_gyro_x'
    id = Column(Integer, primary_key=True)
    row_data = Column(String)
    label = Column(String)

    def __repr__(self):
        return self.label


class BodyGyroY(Base):
    __tablename__ = 'body_gyro_y'
    id = Column(Integer, primary_key=True)
    row_data = Column(String)
    label = Column(String)

    def __repr__(self):
        return self.label


class BodyGyroZ(Base):
    __tablename__ = 'body_gyro_z'
    id = Column(Integer, primary_key=True)
    row_data = Column(String)
    label = Column(String)

    def __repr__(self):
        return self.label
