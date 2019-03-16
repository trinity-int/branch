drop table if exists Events;
drop table if exists Users;
drop table if exists UsersRegistered;

create table Events (
    ID int not null,
    EventName varchar(255) not null,
    EventDate date not null,
    Host varchar(255) not null,
    DateCreated date not null,
    EventLocation varchar(255) not null,
    EventType varchar(255) not null,
    EventDifficulty varchar(255) not null,
    primary key (ID),
    foreign key (Host) references Users(ID)
);

create table Users (
    ID int not null,
    FirstName varchar(255) not null,
    LastName varchar(255) not null,
    UserName varchar(255) not null,
    Email varchar(255) not null,
    PhoneNumber varchar(255),
    Birthday date,
    primary key (ID)
);

create table UsersRegistered (
    EventID int not null,
    UserID int not null,
    primary key (EventID),
    foreign key (EventID) references Events(ID),
    foreign key (UserID) references Users(ID)
)