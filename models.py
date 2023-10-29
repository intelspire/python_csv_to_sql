import enum

from sqlmodel import Field, Column, Enum, SQLModel
from sqlalchemy.dialects.mysql import TEXT, BIGINT
from pydantic import condecimal
from typing import Optional
from datetime import datetime, date, time


class ToastOrderDetails(SQLModel, table=True):
    __tablename__ = "ToastOrderDetails"

    pk: Optional[int] = Field(primary_key=True)
    Location: str = Field(default=None)
    OrderId: int = Field(sa_column=Column(BIGINT), default=None)
    OrderNumber: int = Field(default=None)
    Checks: str = Field(default=None)
    Opened: datetime = Field(default=None)
    NumberOfGuests: int = Field(default=None)
    TabNames: str = Field(default=None)
    DServer: str = Field(default=None)
    DTable: int = Field(default=None)
    RevenueCenter: str = Field(default=None)
    DiningArea: str = Field(default=None)
    Service: str = Field(default=None)
    DiningOptions: str = Field(default=None)
    DiscountAmount: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Amount: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Tax: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Tip: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Gratuity: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Total: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Voided: bool = Field(default=None)
    Paid: datetime = Field(default=None)
    Closed: datetime = Field(default=None)
    DurationOpenedToPaid: time = Field(default=None)
    OrderSource: str = Field(default=None)


class ToastPaymentDetails(SQLModel, table=True):
    __tablename__ = "ToastPaymentDetails"

    pk: Optional[int] = Field(primary_key=True)
    Location: str = Field(max_length=255, default=None)
    PaymentId: int = Field(sa_column=Column(BIGINT), default=None)
    OrderId: int = Field(sa_column=Column(BIGINT), default=None)
    OrderNumber: int = Field(default=None)
    PaidDate: datetime = Field(default=None)
    OrderDate: datetime = Field(default=None)
    CheckId: int = Field(sa_column=Column(BIGINT), default=None)
    CheckNumber: int = Field(default=None)
    TabName: str = Field(max_length=255, default=None)
    DServer: str = Field(max_length=255, default=None)
    DTable: str = Field(max_length=255, default=None)
    DiningArea: str = Field(max_length=255, default=None)
    Service: str = Field(max_length=255, default=None)
    DiningOption: str = Field(max_length=255, default=None)
    HouseAcctNumber: str = Field(max_length=255, default=None)
    Amount: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Tip: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Gratuity: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Total: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    SwipedCardAmount: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    KeyedCardAmount: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    AmountTendered: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Refunded: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    RefundDate: datetime = Field(default=None)
    RefundAmount: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    RefundTipAmount: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    VoidUser: str = Field(max_length=255, default=None)
    VoidApprover: str = Field(max_length=255, default=None)
    VoidDate: datetime = Field(default=None)
    DStatus: str = Field(max_length=255, default=None)
    DType: str = Field(max_length=255, default=None)
    CashDrawer: str = Field(max_length=255, default=None)
    CardType: str = Field(max_length=255, default=None)
    OtherType: str = Field(max_length=255, default=None)
    Email: str = Field(max_length=255, default=None)
    Phone: str = Field(max_length=255, default=None)
    Last4CardDigits: str = Field(max_length=4, default=None)
    VMCDFees: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    RoomInfo: str = Field(max_length=255, default=None)
    Receipt: str = Field(max_length=255, default=None)
    DSource: str = Field(max_length=255, default=None)


class ToastCheckDetails(SQLModel, table=True):
    __tablename__ = "ToastCheckDetails"

    pk: Optional[int] = Field(primary_key=True)
    CustomerId: int = Field(sa_column=Column(BIGINT), default=None)
    Customer: str = Field(max_length=255, default=None)
    CustomerPhone: str = Field(max_length=255, default=None)
    CustomerEmail: str = Field(max_length=255, default=None)
    LocationCode: str = Field(max_length=255, default=None)
    OpenedDate: date = Field(default=None)
    OpenedTime: time = Field(default=None)
    ItemDescription: str = Field(sa_column=Column(TEXT), default=None)
    DServer: str = Field(max_length=255, default=None)
    Tax: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Tender: str = Field(max_length=255, default=None)
    CheckId: int = Field(sa_column=Column(BIGINT), default=None)
    CheckNumber: int = Field(default=None)
    Total: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    CustomerFamily: int = Field(default=None)
    TableSize: int = Field(default=None)
    Discount: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    ReasonOfDiscount: str = Field(max_length=255, default=None)
    Link: str = Field(max_length=255, default=None)


class ToastItemDetails(SQLModel, table=True):
    __tablename__ = "ToastItemDetails"

    pk: Optional[int] = Field(primary_key=True)
    Location: str = Field(max_length=255, default=None)
    OrderId: int = Field(sa_column=Column(BIGINT), default=None)
    OrderNumber: int = Field(default=None)
    SentDate: datetime = Field(default=None)
    OrderDate: datetime = Field(default=None)
    CheckId: int = Field(sa_column=Column(BIGINT), default=None)
    DServer: str = Field(max_length=255, default=None)
    DTable: str = Field(max_length=255, default=None)
    DiningArea: str = Field(max_length=255, default=None)
    Service: str = Field(max_length=255, default=None)
    DiningOption: str = Field(max_length=255, default=None)
    ItemSelectionId: int = Field(sa_column=Column(BIGINT), default=None)
    ItemId: int = Field(sa_column=Column(BIGINT), default=None)
    MasterId: int = Field(sa_column=Column(BIGINT), default=None)
    SKU: str = Field(max_length=255, default=None)
    PLU: str = Field(max_length=255, default=None)
    MenuItem: str = Field(sa_column=Column(TEXT), default=None)
    MenuSubgroups: str = Field(max_length=255, default=None)
    MenuGroup: str = Field(max_length=255, default=None)
    Menu: str = Field(max_length=255, default=None)
    SalesCategory: str = Field(max_length=255, default=None)
    GrossPrice: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Discount: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    NetPrice: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Quantity: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Tax: condecimal(max_digits=10, decimal_places=8) = Field(default=None)
    IsVoid: bool = Field(default=None)
    IsDeferred: bool = Field(default=None)
    IsTaxExempt: bool = Field(default=None)
    TaxInclusionOption: str = Field(max_length=255, default=None)
    DiningOptionTax: str = Field(max_length=255, default=None)
    TabName: str = Field(max_length=255, default=None)


class ToastModifierDetails(SQLModel, table=True):
    __tablename__ = "ToastModifierDetails"

    pk: Optional[int] = Field(primary_key=True)
    Location: str = Field(max_length=255, default=None)
    OrderId: int = Field(sa_column=Column(BIGINT), default=None)
    OrderNumber: int = Field(default=None)
    SentDate: datetime = Field(default=None)
    OrderDate: datetime = Field(default=None)
    CheckId: int = Field(sa_column=Column(BIGINT), default=None)
    DServer: str = Field(max_length=255, default=None)
    TableNumber: int = Field(default=None)
    DiningArea: str = Field(max_length=255, default=None)
    Service: str = Field(max_length=255, default=None)
    DiningOption: str = Field(max_length=255, default=None)
    Item_Selection_Id: int = Field(sa_column=Column(BIGINT), default=None)
    Modifier_Id: int = Field(sa_column=Column(BIGINT), default=None)
    MasterId: int = Field(sa_column=Column(BIGINT), default=None)
    ModifierSKU: str = Field(max_length=255, default=None)
    ModifierPLU: str = Field(max_length=255, default=None)
    ModifierDescription: str = Field(max_length=255, default=None)
    OptionGroupID: int = Field(sa_column=Column(BIGINT), default=None)
    OptionGroupName: str = Field(max_length=255, default=None)
    ParentMenuSelectionItemID: int = Field(sa_column=Column(BIGINT), default=None)
    ParentMenuSelectionDescription: str = Field(max_length=255, default=None)
    SalesCategory: str = Field(max_length=255, default=None)
    GrossPrice: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Discount: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    NetPrice: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Quantity: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    IsVoid: bool = Field(default=None)
    VoidReasonID: int = Field(sa_column=Column(BIGINT), default=None)
    VoidReason: str = Field(max_length=255, default=None)


class AutoClockOutEnum(enum.Enum):
    Yes = "Yes"
    No = "No"


class ToastTimeEntries(SQLModel, table=True):
    __tablename__ = "ToastTimeEntries"

    pk: Optional[int] = Field(primary_key=True)
    Location: str = Field(max_length=255, default=None)
    LocationCode: str = Field(max_length=255, default=None)
    Id: int = Field(sa_column=Column(BIGINT), default=None)
    GUID: str = Field(max_length=36, default=None)
    EmployeeId: int = Field(sa_column=Column(BIGINT), default=None)
    EmployeeGUID: str = Field(max_length=36, default=None)
    EmployeeExternalId: str = Field(max_length=255, default=None)
    Employee: str = Field(max_length=255, default=None)
    JobId: int = Field(sa_column=Column(BIGINT), default=None)
    JobGUID: str = Field(max_length=36, default=None)
    JobCode: str = Field(max_length=255, default=None)
    JobTitle: str = Field(max_length=255, default=None)
    InDate: datetime = Field(default=None)
    OutDate: datetime = Field(default=None)
    AutoClockOut: Optional[AutoClockOutEnum] = Field(
        sa_column=Column(Enum(AutoClockOutEnum))
    )
    TotalHours: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    UnpaidBreakTime: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    PaidBreakTime: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    PayableHours: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    CashTipsDeclared: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    NonCashTips: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    TotalGratuity: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    TotalTips: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    TipsWithheld: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    Wage: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    RegularHours: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    OvertimeHours: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    RegularPay: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    OvertimePay: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    TotalPay: condecimal(max_digits=10, decimal_places=2) = Field(default=None)


class HouseAccountExport(SQLModel, table=True):
    __tablename__ = "HouseAccountExport"

    pk: Optional[int] = Field(primary_key=True)
    HouseAccountGUID: str = Field(max_length=36, default=None)
    HouseAccountCustomerNumber: int = Field(default=None)


class CashEntries(SQLModel, table=True):
    __tablename__ = "CashEntries"

    pk: Optional[int] = Field(primary_key=True)
    Location: str = Field(max_length=255, default=None)
    EntryId: int = Field(sa_column=Column(BIGINT), default=None)
    CreatedDate: datetime = Field(default=None)
    Action: str = Field(max_length=255, default=None)
    Amount: condecimal(max_digits=10, decimal_places=2) = Field(default=None)
    CashDrawer: str = Field(max_length=255, default=None)
    PayoutReason: str = Field(max_length=255, default=None)
    NoSaleReason: str = Field(max_length=255, default=None)
    Comment: str = Field(max_length=255, default=None)
    Employee: str = Field(max_length=255, default=None)
    Employee2: str = Field(max_length=255, default=None)
