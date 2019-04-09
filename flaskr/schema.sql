drop table if exists Events;
drop table if exists Users;
drop table if exists UsersRegistered;

create table Events (
    ID integer primary key autoincrement,
    EventName varchar(255) not null,
    EventDate date not null,
    Host varchar(255) not null,
    DateCreated date not null,
    EventLocation varchar(255) not null,
    EventType varchar(255) not null,
    EventDifficulty varchar(255) not null,
    foreign key (Host) references Users(ID)
);

create table Users (
    ID integer primary key autoincrement,
    FirstName varchar(255) not null,
    LastName varchar(255) not null,
    Email varchar(255) not null,
    Password varchar(255) not null,
    Age integer not null,
    Gender varchar(255) not null
);

create table UsersRegistered (
    EventID integer primary key,
    UserID integer not null,
    foreign key (EventID) references Events(ID),
    foreign key (UserID) references Users(ID)
)