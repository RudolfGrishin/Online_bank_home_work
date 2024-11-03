def get_mask_card_number(card_number: str) -> str:
  """Функция макскирует номера принимаемых карт"""
  if len(card_number) != 16:
    raise ValueError("Неверная длина номера карты")
  if not card_number.isdigit():
    raise ValueError("Номер должен состоять только из цифр")
  return f"{card_number[0:4]} {card_number[4:6]} ** {card_number[12:16]}"

def get_mask_account(account_number: str) -> str:
  """Функция маскирует номер принимаемого счёта"""
  if len(account_number) != 20:
    raise ValueError("Неверная длина номера счёта")
  if not account_number.isdigit():
    raise ValueError("Номер счёта должен состоять только из цифр")
  return f"**{account_number[-5:-1]}"