from pathlib import Path
import yaml
from src.pipeline.citp_pipeline import CITPPipeline

def main():
    cfg=yaml.safe_load(open('configs/default.yaml'))
    print('='*60)
    print(cfg['project']['name'],'Research Framework')
    print('='*60)
    for p in ['outputs/logs','outputs/figures','outputs/tables','outputs/reports']:
        Path(p).mkdir(parents=True,exist_ok=True)
    CITPPipeline().run()
if __name__=='__main__':
    main()
