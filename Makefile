all: build_main_windows build_forms

build_main_windows: package/ui/ui_mainwindow.py package/ui/ui_invoice_details.py package/ui/ui_process_manager_dialog.py

build_forms: package/ui/ui_invoice_form.py package/ui/ui_bill_form.py package/ui/ui_invoice_detail_form.py

package/ui/ui_mainwindow.py: designer/mainwindow.ui
	/usr/lib/qt6/uic -g python designer/mainwindow.ui > package/ui/ui_mainwindow.py
	
package/ui/ui_invoice_form.py: designer/invoice_form.ui
	/usr/lib/qt6/uic -g python designer/invoice_form.ui > package/ui/ui_invoice_form.py

package/ui/ui_bill_form.py: designer/bill_form.ui
	/usr/lib/qt6/uic -g python designer/bill_form.ui > package/ui/ui_bill_form.py

package/ui/ui_process_manager_dialog.py: designer/process_manager_dialog.ui
	/usr/lib/qt6/uic -g python designer/process_manager_dialog.ui > package/ui/ui_process_manager_dialog.py
	
package/ui/ui_invoice_details.py: designer/invoice_details.ui
	/usr/lib/qt6/uic -g python designer/invoice_details.ui > package/ui/ui_invoice_details.py

package/ui/ui_invoice_detail_form.py: designer/invoice_detail_form.ui
	/usr/lib/qt6/uic -g python designer/invoice_detail_form.ui > package/ui/ui_invoice_detail_form.py