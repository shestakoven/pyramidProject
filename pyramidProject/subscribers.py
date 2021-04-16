import transaction


def commit_db(event):
    transaction.commit()
