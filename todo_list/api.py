from ninja import Router

router = Router()


@router.get("healthcheck")
def health_check(request):
    """Retorna se a API está operacional."""
    return {"status": "ok"}
