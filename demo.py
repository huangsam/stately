from stately.contexts import PersonContext
from stately.enums import PersonStateKey


def main():
    # Starts off passive
    person_ctx = PersonContext("John Doe")

    # Starts running and walking actively
    person_ctx.running()
    assert person_ctx.get_state_key() is PersonStateKey.ACTIVE
    person_ctx.walking()
    assert person_ctx.get_state_key() is PersonStateKey.ACTIVE

    # Gets tired from walking and becomes passive
    person_ctx.walking()
    assert person_ctx.get_state_key() is PersonStateKey.PASSIVE

    # Tries walking but cannot walk at all
    person_ctx.walking()
    assert person_ctx.get_state_key() is PersonStateKey.PASSIVE

    # Takes some take to rest
    person_ctx.resting()
    assert person_ctx.get_state_key() is PersonStateKey.PASSIVE

    # Gets back to walking
    person_ctx.walking()
    assert person_ctx.get_state_key() is PersonStateKey.ACTIVE

    # Takes the rest of the day off
    person_ctx.resting()
    assert person_ctx.get_state_key() is PersonStateKey.PASSIVE
    person_ctx.resting()
    assert person_ctx.get_state_key() is PersonStateKey.PASSIVE


if __name__ == '__main__':
    main()
