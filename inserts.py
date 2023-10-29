import pandas as pd
from dateutil.parser import parse

from sqlmodel import Session

from models import (
    ToastOrderDetails,
    ToastPaymentDetails,
    ToastCheckDetails,
    ToastItemDetails,
    ToastModifierDetails,
    ToastTimeEntries,
    HouseAccountExport,
    CashEntries,
)


def insert_toast_order_details(data: pd.DataFrame, session: Session):
    for _, row in data.iterrows():
        obj = ToastOrderDetails(
            Location=row["Location"],
            OrderId=row["Order Id"],
            OrderNumber=row["Order #"],
            Checks=row["Checks"],
            Opened=parse(row["Opened"]) if row["Opened"] else None,
            NumberOfGuests=row["# of Guests"],
            TabNames=row["Tab Names"],
            DServer=row["Server"],
            DTable=row["Table"],
            RevenueCenter=row["Revenue Center"],
            DiningArea=row["Dining Area"],
            Service=row["Service"],
            DiningOptions=row["Dining Options"],
            DiscountAmount=row["Discount Amount"],
            Amount=row["Amount"],
            Tax=row["Tax"],
            Tip=row["Tip"],
            Gratuity=row["Gratuity"],
            Total=row["Total"],
            Voided=row["Voided"],
            Paid=parse(row["Paid"]) if row["Paid"] else None,
            Closed=parse(row["Closed"]) if row["Closed"] else None,
            DurationOpenedToPaid=parse(row["Duration (Opened to Paid)"])
            if row["Duration (Opened to Paid)"]
            else None,
            OrderSource=row["Order Source"],
        )

        session.add(obj)


def insert_toast_payment_details(data: pd.DataFrame, session: Session):
    for _, row in data.iterrows():
        obj = ToastPaymentDetails(
            Location=row["Location"],
            PaymentId=row["Payment Id"],
            OrderId=row["Order Id"],
            OrderNumber=row["Order #"],
            PaidDate=parse(row["Paid Date"]) if row["Paid Date"] else None,
            OrderDate=parse(row["Order Date"]) if row["Order Date"] else None,
            CheckId=row["Check Id"],
            CheckNumber=row["Check #"],
            TabName=row["Tab Name"],
            DServer=row["Server"],
            DTable=row["Table"],
            DiningArea=row["Dining Area"],
            Service=row["Service"],
            DiningOption=row["Dining Option"],
            HouseAcctNumber=row["House Acct #"],
            Amount=row["Amount"],
            Tip=row["Tip"],
            Gratuity=row["Gratuity"],
            Total=row["Total"],
            SwipedCardAmount=row["Swiped Card Amount"],
            KeyedCardAmount=row["Keyed Card Amount"],
            AmountTendered=row["Amount Tendered"],
            Refunded=row["Refunded"],
            RefundDate=parse(row["Refund Date"]) if row["Refund Date"] else None,
            RefundAmount=row["Refund Amount"],
            RefundTipAmount=row["Refund Tip Amount"],
            VoidUser=row["Void User"],
            VoidApprover=row["Void Approver"],
            VoidDate=parse(row["Void Date"]) if row["Void Date"] else None,
            DStatus=row["Status"],
            DType=row["Type"],
            CashDrawer=row["Cash Drawer"],
            CardType=row["Card Type"],
            OtherType=row["Other Type"],
            Email=row["Email"],
            Phone=row["Phone"],
            Last4CardDigits=row["Last 4 Card Digits"],
            VMCDFees=row["V/MC/D Fees"],
            RoomInfo=row["Room Info"],
            Receipt=row["Receipt"],
            DSource=row["Source"],
        )

        session.add(obj)


def insert_toast_check_details(data: pd.DataFrame, session: Session):
    for _, row in data.iterrows():
        obj = ToastCheckDetails(
            CustomerId=row["Customer Id"],
            Customer=row["Customer"],
            CustomerPhone=row["Customer Phone"],
            CustomerEmail=row["Customer Email"],
            LocationCode=row["Location Code"],
            OpenedDate=parse(row["Opened Date"]) if row["Opened Date"] else None,
            OpenedTime=parse(row["Opened Time"]).time() if row["Opened Time"] else None,
            ItemDescription=row["Item Description"],
            DServer=row["Server"],
            Tax=row["Tax"],
            Tender=row["Tender"],
            CheckId=row["Check Id"],
            CheckNumber=row["Check #"],
            Total=row["Total"],
            CustomerFamily=row["Customer Family"],
            TableSize=row["Table Size"],
            Discount=row["Discount"],
            ReasonOfDiscount=row["Reason of Discount"],
            Link=row["Link"],
        )

        session.add(obj)


def insert_toast_item_details(data: pd.DataFrame, session: Session):
    for _, row in data.iterrows():
        obj = ToastItemDetails(
            Location=row["Location"],
            OrderId=row["Order Id"],
            OrderNumber=row["Order #"],
            SentDate=parse(row["Sent Date"]) if row["Sent Date"] else None,
            OrderDate=parse(row["Order Date"]) if row["Order Date"] else None,
            CheckId=row["Check Id"],
            DServer=row["Server"],
            DTable=row["Table"],
            DiningArea=row["Dining Area"],
            Service=row["Service"],
            DiningOption=row["Dining Option"],
            ItemSelectionId=row["Item Selection Id"],
            ItemId=row["Item Id"],
            MasterId=row["Master Id"],
            SKU=row["SKU"],
            PLU=row["PLU"],
            MenuItem=row["Menu Item"],
            MenuSubgroups=row["Menu Subgroup(s)"],
            MenuGroup=row["Menu Group"],
            Menu=row["Menu"],
            SalesCategory=row["Sales Category"],
            GrossPrice=row["Gross Price"],
            Discount=row["Discount"],
            NetPrice=row["Net Price"],
            Quantity=row["Qty"],
            Tax=row["Tax"],
            IsVoid=row["Void?"],
            IsDeferred=row["Deferred"],
            IsTaxExempt=row["Tax Exempt"],
            TaxInclusionOption=row["Tax Inclusion Option"],
            DiningOptionTax=row["Dining Option Tax"],
            TabName=row["Tab Name"],
        )

        session.add(obj)


def insert_toast_modifier_details(data: pd.DataFrame, session: Session):
    for _, row in data.iterrows():
        obj = ToastModifierDetails(
            Location=row["Location"],
            OrderId=row["Order Id"],
            OrderNumber=row["Order #"],
            SentDate=parse(row["Sent Date"]) if row["Sent Date"] else None,
            OrderDate=parse(row["Order Date"]) if row["Order Date"] else None,
            CheckId=row["Check Id"],
            DServer=row["Server"],
            TableNumber=row["Table"],
            DiningArea=row["Dining Area"],
            Service=row["Service"],
            DiningOption=row["Dining Option"],
            Item_Selection_Id=row["Item Selection Id"],
            Modifier_Id=row["Modifier Id"],
            MasterId=row["Master Id"],
            ModifierSKU=row["Modifier SKU"],
            ModifierPLU=row["Modifier PLU"],
            ModifierDescription=row["Modifier"],
            OptionGroupID=row["Option Group ID"],
            OptionGroupName=row["Option Group Name"],
            ParentMenuSelectionItemID=row["Parent Menu Selection Item ID"],
            ParentMenuSelectionDescription=row["Parent Menu Selection"],
            SalesCategory=row["Sales Category"],
            GrossPrice=row["Gross Price"],
            Discount=row["Discount"],
            NetPrice=row["Net Price"],
            Quantity=row["Qty"],
            IsVoid=row["Void?"],
            VoidReasonID=row["Void Reason ID"],
            VoidReason=row["Void Reason"],
        )

        session.add(obj)


def insert_toast_time_entries(data: pd.DataFrame, session: Session):
    for _, row in data.iterrows():
        obj = ToastTimeEntries(
            Location=row["Location"],
            LocationCode=row["Location Code"],
            Id=row["Id"],
            GUID=row["GUID"],
            EmployeeId=row["Employee Id"],
            EmployeeGUID=row["Employee GUID"],
            EmployeeExternalId=row["Employee External Id"],
            Employee=row["Employee"],
            JobId=row["Job Id"],
            JobGUID=row["Job GUID"],
            JobCode=row["Job Code"],
            JobTitle=row["Job Title"],
            InDate=parse(row["In Date"]) if row["In Date"] else None,
            OutDate=parse(row["Out Date"]) if row["Out Date"] else None,
            AutoClockOut=row["Auto Clock-out"],
            TotalHours=row["Total Hours"],
            UnpaidBreakTime=row["Unpaid Break Time"],
            PaidBreakTime=row["Paid Break Time"],
            PayableHours=row["Payable Hours"],
            CashTipsDeclared=row["Cash Tips Declared"],
            NonCashTips=row["Non Cash Tips"],
            TotalGratuity=row["Total Gratuity"],
            TotalTips=row["Total Tips"],
            TipsWithheld=row["Tips Withheld"],
            Wage=row["Wage"],
            RegularHours=row["Regular Hours"],
            OvertimeHours=row["Overtime Hours"],
            RegularPay=row["Regular Pay"],
            OvertimePay=row["Overtime Pay"],
            TotalPay=row["Total Pay"],
        )

        session.add(obj)


def insert_house_account_export(data: pd.DataFrame, session: Session):
    for _, row in data.iterrows():
        obj = HouseAccountExport(
            HouseAccountGUID=row["House Account GUID"],
            HouseAccountCustomerNumber=row["House Account Customer #"],
        )

        session.add(obj)


def insert_cash_entries(data: pd.DataFrame, session: Session):
    for _, row in data.iterrows():
        obj = CashEntries(
            Location=row["Location"],
            EntryId=row["Entry Id"],
            CreatedDate=parse(row["Created Date"]) if row["Created Date"] else None,
            Action=row["Action"],
            Amount=row["Amount"],
            CashDrawer=row["Cash Drawer"],
            PayoutReason=row["Payout Reason"],
            NoSaleReason=row["No Sale Reason"],
            Comment=row["Comment"],
            Employee=row["Employee"],
            Employee2=row["Employee 2"],
        )

        session.add(obj)
