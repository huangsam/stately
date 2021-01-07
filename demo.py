from stately.enums import PersonStateKey
from stately.person import Person


def main():
    # Starts off passive
    person = Person("John Doe")

    # Starts running and walking actively
    person.running()
    assert person.get_state_key() is PersonStateKey.ACTIVE
    person.walking()
    assert person.get_state_key() is PersonStateKey.ACTIVE

    # Gets tired from walking and becomes passive
    person.walking()
    assert person.get_state_key() is PersonStateKey.PASSIVE

    # Tries walking but cannot walk at all
    person.walking()
    assert person.get_state_key() is PersonStateKey.PASSIVE

    # Takes some take to rest
    person.resting()
    assert person.get_state_key() is PersonStateKey.PASSIVE

    # Gets back to walking
    person.walking()
    assert person.get_state_key() is PersonStateKey.ACTIVE

    # Takes the rest of the day off
    person.resting()
    assert person.get_state_key() is PersonStateKey.PASSIVE
    person.resting()
    assert person.get_state_key() is PersonStateKey.PASSIVE


if __name__ == '__main__':
    main()
