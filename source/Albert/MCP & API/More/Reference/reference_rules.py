"""Specification demonstrator. Trusted fixture dictionaries are not real identity/security."""
def run_fixture(state):
    f=[]
    def check(condition,code):
        if not condition: f.append(code)
    check(state['case'] in state['allowedCases'],'case_access_denied')
    check(state['principal']==state['grantRecipient'],'grant_recipient_denied')
    check(not state['grantExpired'],'grant_expired')
    check(state['requestedGraphRevision']==state['graphRevision'],'snapshot_stale')
    check(set(state['requested'])<=set(state['permitted']),'view_access_denied')
    check(not(state['localOnly'] and state['egress']),'egress_denied')
    check(state['sourceExpected']==state['sourceObserved'],'source_digest_mismatch')
    check(state['role']=='human_played','role_not_playable')
    unit=state['offsetUnit']; start=state['start']; length=state['length']; text=state['text']
    try:
        if unit=='codepoints': selected=text[start:start+length]
        elif unit=='utf16': selected=text.encode('utf-16-le')[start*2:(start+length)*2].decode('utf-16-le')
        elif unit=='bytes': selected=text.encode('utf-8')[start:start+length].decode('utf-8')
        else: selected=None
    except UnicodeError: selected=None
    check(selected==state['selected'],'selected_text_mismatch')
    check(len(set(state['exhibitIds']))==1,'cross_exhibit_chunk')
    check(not(state['generationJob'] and state['nextJobState']=='succeeded'),'generation_success_bypass')
    check(state['cancelGeneration']==state['callbackCancelGeneration'],'late_callback_quarantined')
    check(not state['keyAlreadyUsed'] or state['storedDigest']==state['requestDigest'],'idempotency_conflict')
    check(state['writer']!=state['checker'],'checker_not_separate')
    check(all(state[k] for k in ['changedInput','changedArtifact','changedOutcome','resolvedMaterialDefect']),'revision_not_counted')
    check(state['artifactKind']!='witness_packet' or state['packetCategoryMapResolved'],'packet_policy_unresolved')
    scores=state['scores']
    if state['artifactKind']=='podcast_script':
        check(len(scores)==8 and min(scores)>=4.25 and sum(scores)/8>=4.25,'podcast_threshold_failed')
    check(state['seriousFindings']==0,'serious_findings_present')
    check(not state['criticalRegression'],'critical_regression')
    check(not(state['attempts']>=5 and state['countedCycles']<2),'revision_budget_exhausted')
    check(state['approvedDigest']==state['currentDigest'],'stale_approval')
    check(state['humanDecision']!='approve' or state['reviewerAuthenticated'],'human_review_required')
    return {'findings':f,'primary':f[0] if f else None}
