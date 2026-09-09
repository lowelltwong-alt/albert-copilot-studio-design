"""Exact whitespace-token count for this saved Markdown format; not audio measurement."""
from pathlib import Path
import argparse,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
def measure(text):
    turns=re.findall(r'^\*\*HOST_[AB] \[([^]]+)\]:\*\* (.+)$',text,re.M)
    pauses=re.findall(r'^\[PAUSE (\d+) seconds\]$',text,re.M)
    words=sum(len(speech.split()) for _,speech in turns)
    return {'speaker_lines':len(turns),'spoken_whitespace_tokens':words,'pause_count':len(pauses),'pause_seconds':sum(map(int,pauses))}
def main():
    p=argparse.ArgumentParser();p.add_argument('--receipt');a=p.parse_args()
    example='**HOST_A [PC01-A1]:** It is source-bounded.\n\n[PAUSE 8 seconds]\n'
    assert measure(example)=={'speaker_lines':1,'spoken_whitespace_tokens':3,'pause_count':1,'pause_seconds':8}
    source=ROOT/'demo/innovation-demo-script.md';s=source.read_text(encoding='utf-8');m=measure(s)
    assert m['speaker_lines']==43 and m['pause_count']==10
    # Actual order regression: these existing reflection sequences must not pass as practice.
    positions={turn:s.index('['+turn+']') for turn,_ in re.findall(r'^\*\*HOST_[AB] \[([^]]+)\]:\*\* (.+)$',s,re.M)}
    findings=[]
    for chapter,feedback,phrase in [('PC03','PC03-B2','The supported correction is narrow:'),('PC04','PC04-B2','It is the limit:')]:
        start=s.index('## '+chapter);end=s.index('\n## PC',start+1)
        passage=s[start:end];assert passage.index(phrase)<passage.index('[PAUSE ')
        findings.append({'chapter':chapter,'feedback_turn':feedback,'classification':'reflection; feedback already supplied','miscredited_practice_rejected':True})
    result={'scope':'timing convention and two actual order checks only; not a semantic quality gate','script_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'method':'Python str.split() on text after each exact bold HOST_A/HOST_B [turn-id] label; whitespace-delimited tokens; punctuation and hyphen compounds not split; production metadata/labels/cues excluded','measurements':m,'estimated_minutes_by_wpm':{str(rate):round(m['spoken_whitespace_tokens']/rate+m['pause_seconds']/60,3) for rate in [130,145,160]},'order_checks':findings,'tool_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if a.receipt:
        target=(ROOT/a.receipt).resolve();assert target.is_relative_to(ROOT.resolve())
        with target.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
