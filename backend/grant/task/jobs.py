from grant.extensions import db


def proposal_reminder(task_id):
    from grant.task.models import Task
    task = Task.query.filter_by(id=task_id).first()
    from grant.proposal.models import Proposal
    proposal = Proposal.query.filter_by(id=task.blob["proposal_id"]).first()
    # TODO - replace with email
    print(proposal)
    task.completed = True
    db.session.add(task)
    db.session.commit()


JOBS = {
    1: proposal_reminder
}
