from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    abort,
    session,
)

from app.routes.auth import login_required
from app.security.decorators import permission_required

from app.services.invoice_service import InvoiceService
from app.extensions import db
from app.models.patient import Patient
from app.models.invoice_item import InvoiceItem


billing_bp = Blueprint(
    "billing",
    __name__,
    url_prefix="/billing",
)


@billing_bp.route("/")
@login_required
@permission_required("billing:view")
def index():

    query = request.args.get("q","").strip()

    if query:

        invoices = InvoiceService.search(query)

    else:

        invoices = InvoiceService.get_all()

    return render_template(
        "billing/index.html",
        invoices=invoices,
        query=query,
    )


@billing_bp.route("/new")
@login_required
@permission_required("billing:create")
def new():

    patients = (
        Patient.query
        .order_by(
            Patient.first_name,
            Patient.last_name,
        )
        .all()
    )

    return render_template(
        "billing/form.html",
        patients=patients,
    )


@billing_bp.route("/new",methods=["POST"])
@login_required
@permission_required("billing:create")
def create():

    try:

        invoice = InvoiceService.create_invoice(
            request.form,
            session["user_id"],
        )

        flash(
            "Invoice created successfully.",
            "success",
        )

        return redirect(
            url_for(
                "billing.view",
                invoice_id=invoice.id,
            )
        )

    except Exception as e:

        flash(
            str(e),
            "danger",
        )

        return redirect(
            url_for("billing.new")
        )


@billing_bp.route("/<int:invoice_id>")
@login_required
@permission_required("billing:view")
def view(invoice_id):

    invoice = InvoiceService.get_by_id(
        invoice_id
    )

    if invoice is None:
        abort(404)

    return render_template(
        "billing/view.html",
        invoice=invoice,
    )


@billing_bp.route("/<int:invoice_id>/edit")
@login_required
@permission_required("billing:update")
def edit(invoice_id):

    invoice = InvoiceService.get_by_id(
        invoice_id
    )

    if invoice is None:
        abort(404)

    patients = (
        Patient.query
        .order_by(
            Patient.first_name,
            Patient.last_name,
        )
        .all()
    )

    return render_template(
        "billing/edit.html",
        invoice=invoice,
        patients=patients,
    )


@billing_bp.route(
    "/<int:invoice_id>/edit",
    methods=["POST"],
)
@login_required
@permission_required("billing:update")
def update(invoice_id):

    invoice = InvoiceService.get_by_id(
        invoice_id
    )

    if invoice is None:
        abort(404)

    try:

        InvoiceService.update_invoice(
            invoice,
            request.form,
        )

        flash(
            "Invoice updated.",
            "success",
        )

    except Exception as e:

        flash(
            str(e),
            "danger",
        )

    return redirect(
        url_for(
            "billing.view",
            invoice_id=invoice.id,
        )
    )


@billing_bp.route(
    "/<int:invoice_id>/cancel",
    methods=["POST"],
)
@login_required
@permission_required("billing:update")
def cancel(invoice_id):

    invoice = InvoiceService.get_by_id(
        invoice_id
    )

    if invoice is None:
        abort(404)

    InvoiceService.cancel_invoice(
        invoice
    )

    flash(
        "Invoice cancelled.",
        "warning",
    )

    return redirect(
        url_for("billing.index")
    )


@billing_bp.route(
    "/<int:invoice_id>/payment",
    methods=["POST"],
)
@login_required
@permission_required("billing:payment")
def payment(invoice_id):

    invoice = InvoiceService.get_by_id(
        invoice_id
    )

    if invoice is None:
        abort(404)

    try:

        InvoiceService.register_payment(
            invoice,
            request.form,
            session["user_id"],
        )

        flash(
            "Payment received.",
            "success",
        )

    except Exception as e:

        flash(
            str(e),
            "danger",
        )

    return redirect(
        url_for(
            "billing.view",
            invoice_id=invoice.id,
        )
    )


@billing_bp.route(
    "/<int:invoice_id>/item",
    methods=["POST"],
)
@login_required
@permission_required("billing:update")
def add_item(invoice_id):

    invoice = InvoiceService.get_by_id(
        invoice_id,
    )

    if invoice is None:
        abort(404)

    try:

        InvoiceService.add_item(
            invoice,
            request.form,
        )

        flash(
            "Invoice item added.",
            "success",
        )

    except Exception as e:

        flash(
            str(e),
            "danger",
        )

    return redirect(
        url_for(
            "billing.view",
            invoice_id=invoice.id,
        )
    )


@billing_bp.route(
    "/item/<int:item_id>/delete",
    methods=["POST"],
)
@login_required
@permission_required("billing:update")
def delete_item(item_id):

    item = db.session.get(
        InvoiceItem,
        item_id,
    )

    if item is None:
        abort(404)

    invoice_id = item.invoice_id

    try:

        InvoiceService.remove_item(
            item,
        )

        flash(
            "Invoice item removed.",
            "success",
        )

    except Exception as e:

        flash(
            str(e),
            "danger",
        )

    return redirect(
        url_for(
            "billing.view",
            invoice_id=invoice_id,
        )
    )


@billing_bp.route(
    "/<int:invoice_id>/delete",
    methods=["POST"],
)
@login_required
@permission_required("billing:delete")
def delete(invoice_id):

    invoice = InvoiceService.get_by_id(
        invoice_id,
    )

    if invoice is None:
        abort(404)

    try:

        InvoiceService.delete_invoice(
            invoice,
        )

        flash(
            "Invoice deleted successfully.",
            "success",
        )

    except Exception as e:

        flash(
            str(e),
            "danger",
        )

    return redirect(
        url_for("billing.index")
    )
