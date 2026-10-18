import json
import re
import unittest
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'source'
HAN = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]')


def screen_properties():
    source = next((SOURCE / 'src').rglob('*.scm')).read_text(encoding='utf-8')
    return json.loads(source[source.index('{'):source.rindex('}') + 1])['Properties']


def components(node):
    yield node
    for child in node.get('$Components', []):
        yield from components(child)


class SourceTests(unittest.TestCase):
    def test_archive_matches_editable_sources(self):
        with zipfile.ZipFile(SOURCE / 'gps-location-assistant.aia') as archive:
            self.assertIsNone(archive.testzip())
            names = archive.namelist()
            self.assertEqual(len(names), 4)
            for name in names:
                self.assertFalse(name.startswith('/') or '..' in Path(name).parts)
                self.assertIsNone(HAN.search(name))
                self.assertEqual(archive.read(name), (SOURCE / name).read_bytes())

    def test_screen_and_component_references(self):
        nodes = list(components(screen_properties()))
        names = {node['$Name'] for node in nodes}
        self.assertEqual(len(names), len(nodes))
        blocks = ET.parse(next((SOURCE / 'src').rglob('*.bky'))).getroot()
        count = 0
        for node in blocks.iter():
            tag = node.tag.rsplit('}', 1)[-1]
            if tag == 'block':
                count += 1
            if node.get('instance_name'):
                self.assertIn(node.get('instance_name'), names)
            if tag == 'field' and node.get('name') == 'COMPONENT_SELECTOR':
                self.assertIn(node.text, names)
        self.assertEqual(count, 216)
        for node in nodes:
            if 'PhoneNumber' in node:
                self.assertEqual(node['PhoneNumber'], '')
        self.assertIsNone(HAN.search(json.dumps(nodes, ensure_ascii=False)))

    def test_neutral_package_and_english_source(self):
        properties = (SOURCE / 'youngandroidproject' / 'project.properties').read_text(encoding='utf-8')
        self.assertIn('main=appinventor.ai_public_project.gpsa.Screen1', properties)
        for path in SOURCE.rglob('*'):
            self.assertIsNone(HAN.search(path.relative_to(SOURCE).as_posix()))
            if path.suffix in {'.scm', '.bky', '.properties'}:
                self.assertIsNone(HAN.search(path.read_text(encoding='utf-8')))
        self.assertTrue((SOURCE / 'src/appinventor/ai_public_project/gpsa/Screen1.scm').is_file())
        self.assertTrue((SOURCE / 'assets/compass.png').is_file())


if __name__ == '__main__':
    unittest.main()
