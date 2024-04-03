import xml.etree.ElementTree as ET


class XMLHandler:
    def __init__(self, filename=None):
        self.tree = None
        self.root = None
        if filename:
            self.load_xml(filename)

    def load_xml(self, filename):
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()

    def save_to_file(self, filename):
        if self.tree:
            self.tree.write(filename)

    def to_string(self):
        if self.root is not None:
            return ET.tostring(self.root, encoding="unicode", method="xml")
        else:
            return ""

    def from_string(self, xml_string):
        self.root = ET.fromstring(xml_string)
        self.tree = ET.ElementTree(self.root)

    def add_custom_tag(self, tag_name, value=None, attributes=None, parent=None):
        if parent is None:
            parent = self.root
        elif isinstance(parent, str):
            parent = self.root.find(".//" + parent)
            if parent is None:
                raise ValueError(f"Parent tag '{parent}' not found.")
        new_tag = ET.SubElement(parent, tag_name)
        if value is not None:
            new_tag.text = str(value)
        if attributes is not None:
            for key, val in attributes.items():
                new_tag.set(key, str(val))

    def find_parent(self, element):
        for parent in self.root.iter():
            if element in parent:
                return parent

    def remove_custom_tag(self, tag_name):
        for element in self.root.findall(".//" + tag_name):
            parent = self.find_parent(element)
            if parent is not None:
                parent.remove(element)
            else:
                raise ValueError(f"Tag '{tag_name}' does not have a parent.")

    def get_elements_with_attributes(self):
        elements_with_attrs = []
        if self.root is not None:
            for element in self.root.iter():
                if element.attrib:
                    elements_with_attrs.append((element.tag, element.attrib))
        return elements_with_attrs


if __name__ == '__main__':
    handler = XMLHandler()
    handler.load_xml("example.xml")
    xml_string = handler.to_string()
    print(xml_string)

    handler.from_string(xml_string)
    handler.add_custom_tag("custom_tag", value="custom_value", attributes={"attr1": "value1"}, parent="description")
    handler.remove_custom_tag("description")

    elements_with_attrs = handler.get_elements_with_attributes()
    print(elements_with_attrs)

    handler.save_to_file("output.xml")
