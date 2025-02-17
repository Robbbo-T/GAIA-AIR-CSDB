import argparse
import os

def load_template(template_name):
    template_path = os.path.join('templates', f'{template_name}.py')
    if not os.path.exists(template_path):
        raise FileNotFoundError(f'Template {template_name} not found.')
    with open(template_path, 'r') as file:
        template = file.read()
    return template

def replace_placeholders(template, params):
    for key, value in params.items():
        template = template.replace(f'{{{{ {key} }}}}', value)
    return template

def parse_params(params_str):
    params = {}
    for param in params_str.split(','):
        key, value = param.split('=')
        params[key] = value
    return params

def main():
    parser = argparse.ArgumentParser(description='AI-driven code generation system.')
    parser.add_argument('--template', required=True, help='Name of the template to use.')
    parser.add_argument('--output', required=True, help='Output file for the generated code.')
    parser.add_argument('--params', required=True, help='Parameters to replace in the template.')

    args = parser.parse_args()

    template = load_template(args.template)
    params = parse_params(args.params)
    generated_code = replace_placeholders(template, params)

    with open(args.output, 'w') as output_file:
        output_file.write(generated_code)

if __name__ == '__main__':
    main()
