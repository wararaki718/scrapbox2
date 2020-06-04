import torch
from transformers import BertTokenizer, BertModel#, BertForMaskedLM


def main():
    # load pretrained-model
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # tokenize
    text = """
    [CLS] YAGNI is a principle behind the XP practice of \"do the simplest thing that could possibly work\". [SEP]
    """
    print('original text:')
    print(text)
    print()

    tokenized_text = tokenizer.tokenize(text)    
    print('Tokenized text:')
    print(tokenized_text)
    print()

    # vectorize
    token_indices = tokenizer.convert_tokens_to_ids(tokenized_text)
    tensor = torch.Tensor([token_indices]).to(torch.int64)
    print('Tensor:')
    print(tensor)

    # load model
    model = BertModel.from_pretrained('bert-base-uncased')
    model.eval()

    with torch.no_grad():
        outputs = model(tensor)
        encoded_layers = outputs[0]
    
    print('Encoded:')
    print(encoded_layers)
    print()
    print('DONE')


if __name__ == '__main__':
    main()
